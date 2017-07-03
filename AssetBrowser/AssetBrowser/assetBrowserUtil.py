import json
import os
from PySide import QtCore, QtGui


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

class SetAssetTextIcon(object):
    def __init__(self,parent):
        self.parent = parent
        item = QtGui.QListWidgetItem(self.parent)
        item.setText('AtriImage')
        item.setIcon(QtGui.QIcon("E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\icons\\openData.png"))
        item.setSizeHint(QtCore.QSize(75,75))

        item2 = QtGui.QListWidgetItem(self.parent)
        item2.setText('AtriImage2')
        item2.setIcon(QtGui.QIcon("E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\icons\\openData.png"))
        item2.setSizeHint(QtCore.QSize(75,75))

        item3 = QtGui.QListWidgetItem(self.parent)
        item3.setText('AtriImage3')
        item3.setIcon(QtGui.QIcon("E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\icons\\openData.png"))
        item3.setSizeHint(QtCore.QSize(75,75))
        
        
        



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