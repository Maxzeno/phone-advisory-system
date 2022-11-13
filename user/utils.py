from django import forms, db
from random import randint
from . import models
from .models import Q, Recommendation
import my_packages.recommendation as prc
from shortuuid import ShortUUID
import random
import joblib
import json
import pickle


header = [
	'id', 'name', 'brand', 'year', 'price', 'network', 'body_form_factor', 'body_color', 
    'os', 'ram', 'storage', 'display_resolution', 'main_camera_resolution', 'selfie_camera_resolution',
    'battery_capacity', 'battery_duration', 'battery_removable', 'wlan', 'bluetooth', 'gps', 
    'fm_radio', 'fingerprint_sensor', 'water_resistant'
]

header_no_underscore = {'body_form_factor': 'bodyformfactor', 'body_color': 'bodycolor', 
	'display_resolution': 'displayresolution', 'main_camera_resolution': 'maincameraresolution',
	 'selfie_camera_resolution':'selfiecameraresolution',
	'battery_capacity': 'batterycapacity', 'battery_duration':'batteryduration', 'fm_radio': 'fmradio', 
	'fingerprint_sensor': 'fingerprintsensor', 'water_resistant': 'waterresistant',
	'wlan': 'wlan', 'bluetooth':'bluetooth','gps':'gps','storage':'storage','ram':'ram', 'os':'os',
	'network':'network','price':'price','year':'year','brand':'brand','name':'name','id':'id', 
	'battery_removable':'batteryremovable'
}


def remove_none_in_dict(dct):
	for k, v in dct.items():
		if not v:
			del dct[k]
	return 'done'


def wordify(string):
	num_d = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
		'7':'seven', '8':'eight', '9':'nine'}

	new_word = ''
	for i in string:
		if num_d.get(i):
				new_word += num_d.get(i)
		else:
			new_word += i
	return new_word


class Filter():
	def process(self, request, index_zero=True):
		if request:
			data = dict(request)
			data.pop('csrfmiddlewaretoken', False)
			data.pop('page', False)
			data.pop('name', False)
			data.pop('id', False)

			if data:
				checkboxlist = ['battery_removable', 'wlan', 'bluetooth', 'gps', 'fm_radio', 'fingerprint_sensor', 'water_resistant']

				query_str = ''
				params = ''
				filter_data = {}
				for k, v in data.items():
					if index_zero:
						val = v[0]
					else:
						val = v

					if val != None:
						if k == 'price' and val:
							query_str += f'Q({k}__lte={float(val)}) & '
							params += f'&{k}={val}'
							filter_data[k] = val

						elif k not in checkboxlist:
							query_str += f'Q({k}__contains=\'{str(val)}\') & '
							params += f'&{k}={val}'
							filter_data[k] = val

						else:
							query_str += f'Q({k}=\'{str(True if val else False)}\') & '
							params += f'&{k}={str(True if val else False)}'
							filter_data[k] = True if str(val) else False

				return {'query_str': query_str[:-3] if query_str else 'Q()', 'params': params, 'filter_data': filter_data}
			return {'query_str': 'Q()', 'params': '', 'filter_data': {}}

		return {'query_str': 'Q()', 'params': '', 'filter_data': {}}


	def userfilter(self, request, query):
		is_auth = request.user.is_authenticated
		if is_auth:
			query['user_id'] = request.user
		else:
			anonymous_user_id = request.session.get('anonymous_user_id')
			if anonymous_user_id:
				query['anonymous_user_id'] = anonymous_user_id
			else:
				query['anonymous_user_id'] = request.session['anonymous_user_id'] = ShortUUID().random(length=50)

		if not query.get('price'):
			query.pop('price', False)
		models.Userfilter.objects.create(**query)

		return 'done'


	def recom(self, request, query_str, query, lm, active_page):
		if query:
			self.userfilter(request, query)
		if request.user.is_authenticated:
			filters = models.Userfilter.objects.filter(user_id=request.user.id).order_by('-date_added').values()[:8]
		else:
			if request.session.get('anonymous_user_id') != None:
				filters = models.Userfilter.objects.filter(
					anonymous_user_id=request.session.get('anonymous_user_id')).order_by('-date_added').values()[:8]
			else:
				filters = []

		# if query_str == 'Q()' and filters:

		get_pickled = self.get_pickle(request)

		if query_str == 'Q()' and get_pickled and active_page > 1:
			model_phone_list = []
			for i in get_pickled[lm*(active_page-1): lm*active_page]:
				the_phone = models.Phones.objects.filter(id=i).first()
				if the_phone:
					model_phone_list.append(the_phone)

			return model_phone_list, len(get_pickled)

		all_recommendations = []

		for a_filter in filters:
			the_id = []
			tags = []

			a_filter.pop('user_id_id', None)
			a_filter.pop('anonymous_user_id', None)
			a_filter.pop('date_added', None)
			choose = models.Phones.objects.filter(eval(self.process(a_filter, False)['query_str'])).values_list('id')
			representing_item_id = random.choice(choose)[0] if choose else None

			if representing_item_id != None:

				phones = models.Phones.objects.values(*header)

				for phone in phones:
					feat = ''

					for k, v in phone.items():
						if k == 'id':
							the_id.append(v)
							continue

						if a_filter[k] != None and a_filter[k] != '' :
							feat +=  k + wordify(str(phone[k])) + ' '
					tags.append(feat.strip())

				itemsInitialise = prc.ItemData()

				sample_items_data = {
					"the_id": the_id,
		            "tags": tags
		        }

				itemData = itemsInitialise.setData(
					data = sample_items_data,
					itemNameField = 'the_id',
					itemTagField = 'tags',
					)

				similarItemInit = prc.SimilarItem(itemData)
				recommendations = similarItemInit.similarItem(representing_item_id, len(phones))

				all_recommendations += recommendations

		all_recommendations = random.sample(all_recommendations, len(all_recommendations))
		all_recommendations.sort(key=lambda x: abs(x[1]), reverse=True)

		phone_ids = []

		for i in all_recommendations:
			if i[0] not in phone_ids:
				phone_ids.append(i[0])

		self.set_pickle(request, phone_ids)

		model_phone_list = []
		for i in phone_ids[lm*(active_page-1): lm*active_page]:
			the_phone = models.Phones.objects.filter(id=i).first()
			if the_phone:
				model_phone_list.append(the_phone)

		if query_str == 'Q()' and filters and len(phone_ids) > 0:

			return model_phone_list, len(phone_ids)

		else:
			matched_phones = models.Phones.objects.filter(eval(query_str)).all()
			return matched_phones[lm*(active_page-1): lm*active_page], len(matched_phones)


	def set_pickle(self, request, data):
		picked = pickle.dumps(data)
		if request.user.is_authenticated:
			found = Recommendation.objects.filter(user_id=request.user.id)
			if found:
				found.update(recommendation=picked)
			else:
				anonymous_user_id = request.session.get('anonymous_user_id')
				anonymous_user = Recommendation.objects.filter(anonymous_user_id=anonymous_user_id)
				if anonymous_user:
					anonymous_user.update(user_id=request.user, recommendation=picked)

				else:
					recom = Recommendation.objects.create(recommendation=picked, user_id=request.user)


		else:
			anonymous_user_id = request.session.get('anonymous_user_id')
			if anonymous_user_id:
				anonymous_user = Recommendation.objects.filter(anonymous_user_id=anonymous_user_id)
				if anonymous_user:
					anonymous_user.update(recommendation=picked)

				elif anonymous_user_id:
					recom = Recommendation.objects.create(recommendation=picked, anonymous_user_id=anonymous_user_id)

				else:
					anonymous_user_id = request.session['anonymous_user_id'] = ShortUUID().random(length=50)
					recom = Recommendation.objects.create(recommendation=picked, anonymous_user_id=anonymous_user_id)

		return 'Done'


	def get_pickle(self, request):
		anonymous_user_id = request.session.get('anonymous_user_id')
		if request.user.is_authenticated:
			found = Recommendation.objects.filter(user_id=request.user.id).first()
			if found:
				return pickle.loads(found.recommendation)
			else:
				return False

		elif anonymous_user_id:
			found = Recommendation.objects.filter(anonymous_user_id=anonymous_user_id).first()
			if found:
				print(found.recommendation)
				print(type(found.recommendation))
				return pickle.loads(found.recommendation)
			else:
				return False

		else:
			return False


def know_anonymous(request):
		anonymous_user_id = request.session.get('anonymous_user_id')
		if anonymous_user_id:
			update_user_id = models.Userfilter.objects.filter(anonymous_user_id=anonymous_user_id)
			if update_user_id.all():
				if request.user.id:
					update_user_id.update(user_id=request.user.id)
					return 'updated'
				else:
					return 'not updated'
			else:
				return 'up to date'

		else:
			'not found'


def randomise(any_iterable):
	return random.choice(any_iterable)


def name_phone_and_brand(brand, als, nums):
	the_brand = random.choice(brand)
	return the_brand, the_brand + ' ' + random.choice(nums) + ' ' + random.choice(als)


def length_favourite(request):
	favourite = request.COOKIES.get('favourite')
	if favourite:
		list_favourite = json.loads(favourite)
	else:
		list_favourite = []

	return len(list_favourite)


def choice_field_tuple(col: str, default: str=None) -> list :
	# try:
	if default:
		q = [ (i[0], i[0]) for i in models.Phones.objects.values_list(col).distinct() if i[0] != None ]
		try:
			q.sort()
		except TypeError:
			pass
		q.insert(0, ('', default))
		return q

	q = [ (i[0], i[0]) for i in models.Phones.objects.values_list(col).distinct() ]
	q.sort()
	# except db.utils.OperationalError:
		# q = ()

	return q


def range_dict(active_page, pages):
	dct = {'begin': active_page - 1 if active_page > 1 else 1, 'end': active_page + 1 if active_page < pages else active_page}

	pages_on_sides = 2

	if active_page + pages_on_sides >= pages and active_page - pages_on_sides <= 1:
		dct['range_start'] = 1
		dct['range_stop'] = pages + 1
	elif active_page + pages_on_sides > pages:
		dct['range_start'] = (active_page - pages_on_sides) - ((active_page + pages_on_sides) - pages)
		dct['range_stop'] = pages + 1
	elif active_page - pages_on_sides < 1:
		dct['range_start'] = 1
		dct['range_stop'] = abs(active_page - pages_on_sides -1) +  active_page + pages_on_sides + 1
	else:
		dct['range_start'] = active_page - pages_on_sides
		dct['range_stop'] = active_page + pages_on_sides + 1

	return dct
