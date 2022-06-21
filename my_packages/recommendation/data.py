

class Item(object):
	"""docstring for Item"""
	def __init__(self, itemName_list, itemTags_list=[], itemDesc_list=[]):
		self.itemNames = itemName_list
		self.itemTags = itemTags_list
		self.itemDescs = itemDesc_list


class Users(object):
	"""docstring for User"""
	def __init__(self, userIds_list, triedItems_list):
		self.userIds = userIds_list
		self.triedItems = triedItems_list
		
		
