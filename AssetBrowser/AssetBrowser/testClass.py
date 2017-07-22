#import json
#import os


#jsonFile =  'E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\rw.json'
##jsonFile  = (os.getcwd ()+'\\assetDataBase.json')
#assetPath =  'E:\\myProjects\\ProjectAssets\\'


#class jsonDataHandler:
#    def __init__(self,jsonFile):
#        self.jsonFile =  jsonFile 
#        self.jObj = json.loads(open(self.jsonFile).read())
        

#    def getCategoryObjInfo(self,category,keyInfo):
#        self.objectInfo = []        
#        objects =  self.jObj[category].keys() 
#        for j in range(0,len(objects)):
#            self.objectInfo.append(self.jObj[category][objects[j]][keyInfo])
#        return self.objectInfo

#    def addKey(self,key):
#        self.jObj.update(key)

#    def removekey(self,key):
#        del self.jObj[key]
        
#    def addCategoryObj(self,category,keyInfo):
#        keyDict = {category: {keyInfo[0] : { "name" : keyInfo[0], "filePath" : keyInfo[1] , "image" : keyInfo[2]}}}
#        self.addKey(keyDict)
    
#    def writeJson(self,assetData):
#        with open(self.jsonFile ,'w') as outfile:
#            json.dump(assetData,outfile,indent=4,sort_keys = True)
           

        
#datH =  jsonDataHandler(jsonFile)
#assetData =  datH.getKeys()

#moreCapitals  =  {'Germany': 'Berlin','UK' : 'London', 'India' : 'Delhi' }

#moreDict  =  { "RigAppend": { "NewRig" : { "name" : "Human", "filePath" : "SomeWhere" , "image" : "yes"}},
#               "MobusAppend": { "NewMobu" : {"name" : "Mobu", "filePath" : "where", "image": "No"}}}

#keyAbstract  = {category: {categoryObj : { "name" : name, "filePath" : filePath , "image" : image}}}

#datH.addKey(moreCapitals)
#datH.addKey(moreDict)

#datH.removekey('NewJObj')
#datH.removekey('MobusAppend')

#datH.addCategoryObj('NewJObj2',['newObjName2','newObjactFilePath2','NewObjectImage2'])

#datH.writeJson(datH.jObj)

#print datH.jObj




#print datH

#print type(datH)

#print assetData
#print type(assetData) 

#del datH['UK']



#with open('rw.json','w') as outfile:
#    json.dump(datH.jObj,outfile)


for i in range(0,10):
    if (i % 2 == 0): 
        print 'even'
    else:
       print 'odd'
    
    
        

    
    
