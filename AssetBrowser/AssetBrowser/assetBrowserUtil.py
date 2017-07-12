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

    def getCategory(self):
        self.category =  []
        #jsonObj = self.readJson()
        for items in self.jObj:
            self.category.append(items)
        return self.category        

    def getCategoryObjInfo(self,category,keyInfo):
        self.objectInfo = []        
        objects =  self.jObj[category].keys() 
        for j in range(0,len(objects)):
            self.objectInfo.append(self.jObj[category][objects[j]][keyInfo])
        return self.objectInfo

    def addCategory(self,category):
        catagories = getCategory()
        print catagories 


    def writeJson(self):
        with open(self.jsonFile ,'w') as outfile:
            json.dump(assetData,outfile,indent=4)


jDataH =  jsonDataHandler(jsonFile)




class UiUpdate:
    
    def uiInit(self,listWidget):
        self.categories = jDataH.getCategory()
        listWidget.addItems(self.categories)
        #print self.categories 
        listWidget.setCurrentRow(5)

    def changeViewMode(self,listWidget,mode):
        
        if mode == 1:
            listWidget.setViewMode(QtGui.QListView.IconMode)            
        else:
            listWidget.setViewMode(QtGui.QListView.ListMode)

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

    def cleanItems(self,listWidget):
        pass





class GetUiInfo:
    
    def getSelectdItem(self):
        pass 

