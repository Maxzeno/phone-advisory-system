from py_recommendation.item_profile import ItemProfile

class UserProfile(ItemProfile):
    """docstring for UserProfile"""
    def __init__(self, itemData, usersData):
        super().__init__(itemData)
        self.usersData = usersData
    
    def generate_userProfile(self, itemIndices):
        filtered = self.itemProfile[itemIndices, :].toarray()
        numer = filtered.sum(axis=0)
        denom = filtered.shape[0]
        
        user_profile = numer/denom

        user_profile = user_profile.reshape((1,user_profile.shape[0]))
        return user_profile 
        