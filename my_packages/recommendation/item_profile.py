from sklearn.feature_extraction.text import CountVectorizer


class ItemProfile():
	"""docstring for ItemProfile"""
	def __init__(self, itemData):
		self.itemData = itemData
		if self.itemData.itemTags:
			self.itemProfile = self.count_vec()

	def count_vec(self):
		count_ = CountVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
		return count_.fit_transform(self.itemData.itemTags)
