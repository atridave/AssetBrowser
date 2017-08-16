import json
import os,sys
from PySide import QtCore, QtGui
import addCategoryUI
import addAssetWindowUI
import icons_rc

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
        items = []
        for index in xrange(listWidget.count()):
             items.append(listWidget.item(index))             
        labels = [i.text() for i in items]
        


    def changeViewMode(self,listWidget,mode):
        
        if mode == 1:
            listWidget.setViewMode(QtGui.QListView.IconMode)            
        else:
            listWidget.setViewMode(QtGui.QListView.ListMode)

    def itemColors(self,listWidget):
        colors = ['#1d334b', '#747572']
        item =  QtGui.QListWidgetItem(listWidget)
        if (i % 2 == 0):
            item.setBackground(QtGui.QColor(colors[0]))
        else:
            item.setBackground(QtGui.QColor(colors[1]))


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

    def invokeAddCategoryUi(self,listWiget):
        categoryAddUI =  addCategoryDialog(listWiget)

    def invokeAssetContextMenu(self,listWiget,point):
        addContextManu().myConMenu(point)

    def invokeAddAssetUI(self,index):
        self.addAssetWin = addAseetUI(index)
        self.addAssetWin.show()
        


 
class addCategoryDialog(QtGui.QDialog,addCategoryUI.Ui_addCategory):
    def __init__(self,listWiget, parent = None):
        super(addCategoryDialog, self).__init__(parent)
        self.setupUi(self)
        self.listWiget  =  listWiget
        self.addButton.clicked.connect(self.addCategory)
        self.addlineEdit.setFocus()
        self.exec_()   


    def addCategory(self):
        categoryName = self.addlineEdit.text()        
        ui =  UiUpdate()
        ui.addCategory(categoryName)
        self.listWiget.clear()
        ui.uiInit(self.listWiget)
        
        newItem = self.listWiget.findItems(categoryName, QtCore.Qt.MatchContains)
        for item in newItem:
            itemRow = self.listWiget.row(item)
        self.listWiget.clear()
        ui.uiInit(self.listWiget,itemRow) 

        self.close()

        
class addAseetUI(QtGui.QMainWindow,addAssetWindowUI.Ui_addAssetWindow):
    def __init__(self,index, parent = None):
        super(addAseetUI, self).__init__(parent)
        self.setupUi(self)
        self.category = jDataH.jObj.keys()
        self.categoryComboBox.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.categoryComboBox.addItems(self.category)
        self.categoryComboBox.model().sort(0)
        self.categoryComboBox.setCurrentIndex(index)
        self.assetPathButton.clicked.connect(self.openFileBrowser)
        self.assetImageButton.clicked.connect(self.openFileBrowser)

    def openFileBrowser(self):
        path  =  'E:\myProjects\ProjectAssets'
        dir = '.'
        QtGui.QFileDialog.getOpenFileName(self,'chooseFile',dir = path,filter = "maya files (*.ma)")

    def openImageBrowser(self):
        print 'Hello'
        path  =  'E:\user\atri\AssetBrowser\AssetBrowser\AssetBrowser\assetIcons'
        #dir = '.'
        print path
        QtGui.QFileDialog.getOpenFileName(self,'chooseFile',dir = path,filter = "maya files (*.ma)")

        
        
    







