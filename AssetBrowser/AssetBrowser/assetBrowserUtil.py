import json
import os
jFile =  'E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\assetDataBase.json'
jFile  = (os.getcwd ()+'\\assetDataBase.json')




def readJson(jFile):
    rFile = open(jFile).read()
    return (json.loads(rFile))

def getCategory(jsonObj):
    category =  []
    for items in jsonObj:
        category.append(items)
    return category

def getCategoryObjInfo(jsonObj,category,keyInfo):
    objectInfo = []
    for i in range(0,len(category)):
        objects =  jsonObj[category[i]].keys()        
        for j in range(0,len(objects)):
            objectInfo.append(jsonObj[category[i]][objects[j]][keyInfo])
    return objectInfo
    

#jObj =  readJson(jFile)
#keyInfo =  getCategoryObjInfo(jObj,(getCategory(jObj)),'image')
#print keyInfo