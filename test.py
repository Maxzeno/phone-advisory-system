import py_recommendation as prc
# import numpy as np
import pandas as pd
# from user.models import Phones



itemsInitialise = prc.ItemData()

# ### file

# itemData = itemsInitialise.setData_file(
#     filePath = "phoness.csv",
#     # itemName_col = 'id',
#     itemNameField = 'id',
#     # itemTag_col = 'name',
#     itemTagField='name',
#     fileType = 'csv'
#     )


# similarItemInit = prc.SimilarItem(itemData)

# print(similarItemInit)

# recommendation = similarItemInit.similarItem('onezero')
# print(recommendation)



### no file

sample_items_data = {"title":['Place-A','Place-B','Place-C','Place-D','Place-E','Place-F','Place-G'],
            "tags":[
                'brandGeonee yeartwozeroonetwo pricefivesixseven.zero networktwog bodyformbar bodycolorcyan osandroid ramfourgb storageonesixgb displayresolutiontwofourfourzeroxonefivefourzero maincameraresolutiononetwomp selfiecameraresolutiononesixmp batterycapacityonezerozerozeromah batterdurationfoureighthours waterresistantFalse fingerprintsensorFalse batteryremovableFalse wlanTrue bluetoothTrue gpsTrue fmradioFalse',
                'brandInfinix yeartwozerotwozero priceeighteight.zero networktwog bodyformflip bodycolorcyan osios rameightgb storagefourgb displayresolutiontwofourfourzeroxonefivefourzero maincameraresolutiontwozeromp selfiecameraresolutiontwozeromp batterycapacityfourzerozerozeromah batterdurationfoureighthours waterresistantFalse fingerprintsensorFalse batteryremovableTrue wlanFalse bluetoothFalse gpsFalse fmradioFalse',
                'brandSamsung yeartwozerozeroseven pricetwozerozero.zero networktwog bodyformflip bodycolororange osios ramonegb storagethreetwogb displayresolutiononesixzerozeroxonetwozerozero maincameraresolutionfourmp selfiecameraresolutiontwozeromp batterycapacityfourzerozerozeromah batterdurationthreesixhours waterresistantFalse fingerprintsensorFalse batteryremovableFalse wlanFalse bluetoothTrue gpsTrue fmradioTrue',
                'brandTecno yeartwozerotwotwo pricetwozerozero.zero networkfourg bodyformbar bodycolorred oswindows rameightgb storageeightgb displayresolutiononesixeightzeroxonezerofivezero maincameraresolutiontwozeromp selfiecameraresolutiontwozeromp batterycapacityonezerozerozeromah batterdurationfoureighthours waterresistantFalse fingerprintsensorTrue batteryremovableFalse wlanTrue bluetoothFalse gpsTrue fmradioTrue',
                'brandSamsung yeartwozerotwozero pricetwozerothreesix.zero networkfourg bodyformbar bodycolorcyan osios ramfourgb storageeightgb displayresolutiononesixeightzeroxonezerofivezero maincameraresolutiononefourmp selfiecameraresolutioneightmp batterycapacitytwozerozerozeromah batterdurationthreesixhours waterresistantFalse fingerprintsensorFalse batteryremovableFalse wlanTrue bluetoothTrue gpsFalse fmradioTrue',
                'brandGeonee yeartwozerotwotwo priceeighteight.zero networkfourg bodyformflip bodycolorgold oswindows ramzero.storagefivegb displayresolutiononesixgboetwoeightzero maincameraresolutionx selfiecameraresolutiononezerotwofour batterycapacityfourmp batterdurationonetwomp waterresistantmah fingerprintsensoratterycapacityFalse batterydurationTrue batteryremovableFalse wlanFalse bluetoothFalse gpsFalse fmradioTrue',
				'brandInfinix yeartwozerotwozero priceeighteight.zero networktwog bodyformflip bodycolorcyan osios rameightgb storagefourgb displayresolutiontwofourfourzeroxonefivefourzero maincameraresolutiontwozeromp selfiecameraresolutiontwozeromp batterycapacityfourzerozerozeromah batterdurationfoureighthours waterresistantFalse fingerprintsensorFalse batteryremovableFalse wlanTrue bluetoothFalse gpsFalse fmradioFalse',  
            ]
           }


itemData = itemsInitialise.setData(
    data = sample_items_data,
    itemNameField = 'title',
    itemTagField = 'tags',
    )

similarItemInit = prc.SimilarItem(itemData)

recommendation = similarItemInit.similarItem('Place-B', 7)
print(recommendation)




##### from database


# def wordify(array_type):
# 	num_d = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
# 		'7':'seven', '8':'eight', '9':'nine'}
# 	new = []
# 	for word in array_type:
# 		new_word = ''
# 		for i in str(word):
# 			if num_d.get(i):
# 				new_word += num_d.get(i)
# 			else:
# 				new_word += i
# 		new.append(new_word)
# 	return new


# def data():
# 	header = [
# 		'id', 'name', 'brand', 'year', 'price', 'network', 'body_form_factor', 'body_color', 
#         'os', 'ram', 'storage', 'display_resolution', 'main_camera_resolution', 'selfie_camera_resolution',
#         'battery_capacity', 'battery_duration', 'battery_removable', 'wlan', 'bluetooth', 'gps', 
#         'fm_radio', 'fingerprint_sensor', 'water_resistant'
#         ]

# 	phones = Phones.objects.values_list(*header)[:20]

# 	writer.writerow(header+['feature'])

# 	print(phones)

# 	for phone in phones:
# 		new = wordify(list(phone))
# 		ft = {}
# 		ft['title'] = []
# 		ft['tags'] = []
# 		print(new)
# 		feature = ''
# 		for i in new[1:]:
# 			print(i)
# 			feature = feature + ' ' + str(i)
# 			print(feature)
# 		print(feature)
# 		ft['tags'].append(feature)
# 		ft['title'].append(phone.id)

# 		print(new)

# 	return ft





# ### no file

# sample_items_data = data()

# print(sample_items_data)
# itemData = itemsInitialise.setData(
#     data = sample_items_data,
#     itemNameField = 'title',
#     itemTagField = 'tags',
#     )

# similarItemInit = prc.SimilarItem(itemData)

# recommendation = similarItemInit.similarItem('Place-D')
# print(recommendation)