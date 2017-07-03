import json
import os


class jsonDataHandler(object):
    def __init__(self):
        self.jasonFile =  'E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\assetDataBase.json'
        #self.jasonFile  = (os.getcwd ()+'\\assetDataBase.json')

    
    def readJson(self):
        self.rFile = open(self.jasonFile).read()
        return json.loads(self.rFile)

    def getCategory(self):
        self.category =  []
        jsonObj = self.readJson()
        for items in jsonObj:
            self.category.append(items)
        return self.category        

    def getCategoryObjInfo(self,category,keyInfo):
        self.objectInfo = []
        jsonObj = self.readJson()
        objects =  jsonObj[category].keys() 
        for j in range(0,len(objects)):
            self.objectInfo.append(jsonObj[category][objects[j]][keyInfo])
        return self.objectInfo



#def readJson(jFile):
#    rFile = open(jFile).read()
#    return (json.loads(rFile))

#def getCategory(jsonObj):
#    category =  []
#    for items in jsonObj:
#        category.append(items)
#    return category

#def getCategoryObjInfo(jsonObj,category,keyInfo):
#    objectInfo = []
#    for i in range(0,len(category)):
#        objects =  jsonObj[category[i]].keys()        
#        for j in range(0,len(objects)):
#            objectInfo.append(jsonObj[category[i]][objects[j]][keyInfo])
#    return objectInfo
    

#jObj =  readJson(jFile)
#keyInfo =  getCategoryObjInfo(jObj,(getCategory(jObj)),'image')
#print keyInfo