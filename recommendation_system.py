import py_recommendation as prc
import pandas as pd
# import joblib

itemsInitialise = prc.ItemData()

# df = pd.read_csv("phoness.csv")
# print(df.shape)
# df.head()

itemData = itemsInitialise.setData_file(
    filePath = "phoness.csv",
    itemNameField = 'id',
    itemTagField='feature',
    fileType = 'csv'
    )


similarItemInit = prc.SimilarItem(itemData)

# joblib.dump(similarItemInit, "phones.joblib")

recommendation = similarItemInit.similarItem(1)
print(recommendation)
