import json
import os


jsonFile =  'E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\assetDataBase.json'
#self.jasonFile  = (os.getcwd ()+'\\assetDataBase.json')
assetPath =  'E:\\myProjects\\ProjectAssets\\'


class jsonDataHandler:
    def __init__(self,jsonFile):
        self.jsonFile =  jsonFile 
        self.jObj = json.loads(open(self.jsonFile).read())
        
datH =  jsonDataHandler(jsonFile)
assetData =  datH.jObj

with open('rw.json','w') as outfile:
    json.dump(assetData,outfile,indent=4)

