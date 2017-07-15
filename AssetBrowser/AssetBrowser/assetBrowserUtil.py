import json
import os
from PySide import QtCore, QtGui

jsonFile =  'E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\assetDataBase.json'
#self.jasonFile  = (os.getcwd ()+'\\assetDataBase.json')
assetPath =  'E:\\myProjects\\ProjectAssets\\'


class jsonDataHandler:
    def __init__(self,jsonFile):
        self.jsonFile =  jsonFile 
        self.jObj = json.loads(open(self.jsonFile).read())

    def writeJson(self,assetData):
        with open(self.jsonFile ,'w') as outfile:
            json.dump(assetData,outfile,indent=4,sort_keys = True)        

    def getCategoryObjInfo(self,category,keyInfo):
        self.objectInfo = []        
        objects =  self.jObj[category].keys() 
        for j in range(0,len(objects)):
            self.objectInfo.append(self.jObj[category][objects[j]][keyInfo])
        return self.objectInfo

    def addKey(self,key):
        self.jObj.update(key)
        self.writeJson(self.jObj)

    def removekey(self,key):
        del self.jObj[key]
        self.writeJson(self.jObj)
        

    def addCategoryObj(self,category,keyInfo=None):
        if keyInfo == None:
            keyInfo =  ['name','filePath','image']
        keyDict = {category: {keyInfo[0] : { "name" : keyInfo[0], "filePath" : keyInfo[1] , "image" : keyInfo[2]}}}
        self.addKey(keyDict)
            
    



jDataH =  jsonDataHandler(jsonFile)




class UiUpdate:
    
    def uiInit(self,listWidget,selectRow=None):
        self.categories = jDataH.jObj.keys()
        listWidget.addItems(self.categories)
        self.sortItems(listWidget)        
       
        if selectRow == None :
            selectRow = 0
        listWidget.setCurrentRow(selectRow)

    def changeViewMode(self,listWidget,mode):
        
        if mode == 1:
            listWidget.setViewMode(QtGui.QListView.IconMode)            
        else:
            listWidget.setViewMode(QtGui.QListView.ListMode)


    def addCategory(self,category):
        jDataH.addCategoryObj(category)


    def removeCategory(self,category):
        jDataH.removekey(category)

    def updateListIteams(self,parentWidget,itemName,itemIcon,itemHSize=None,itemVSize=None):
        if itemHSize or itemVSize == None : 
            itemHSize = itemVSize = 150

        self.parentWidget =  parentWidget
        self.parentWidget.setIconSize(QtCore.QSize(itemVSize,itemVSize))
        
        item =  QtGui.QListWidgetItem(self.parentWidget)
        item.setText(itemName)
        item.setIcon(QtGui.QIcon(itemIcon))       
       

    def setItems(self,listWidget,category):
        name =  jDataH.getCategoryObjInfo(category,'name')
        image = jDataH.getCategoryObjInfo(category,'image')

        for i in range(0,len(name)):
            self.updateListIteams(listWidget,name[i],image[i])

        self.sortItems(listWidget)


    def sortItems(self,listWidget):
        listWidget.setSortingEnabled(True)
        listWidget.sortItems()


 





class GetUiInfo:
    
    def getSelectdItem(self):
        pass 

