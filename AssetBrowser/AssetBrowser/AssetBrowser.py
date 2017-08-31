from PySide.QtCore import *
from PySide.QtGui import *
import sys
import AssetBrowserUI
import assetBrowserUtil as abUtil
import icons_rc



class mainWindow(QMainWindow,AssetBrowserUI.Ui_AssetBrowser):
    def __init__(self, parent =None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.uiUpdate = abUtil.UiUpdate()
        self.uiUpdate.uiInit(self.categorylistWidget,2)
        self.uiUpdate.changeViewMode(self.assetlistWidget,1)
        itemName =  self.categorylistWidget.currentItem().text()       
        self.uiUpdate.setItems(self.assetlistWidget,itemName)        
        self.categorylistWidget.itemClicked.connect(self.updateUI)
        self.addButton.clicked.connect(self.addCategory)
        self.removeButton.clicked.connect(self.removeCategory)       
        self.assetlistWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self.assetlistWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.assetContextMenu)        
    

    def updateUI(self):
        self.assetlistWidget.clear()
        itemName =  self.categorylistWidget.currentItem().text()
        self.uiUpdate.setItems(self.assetlistWidget,itemName)

    def addCategory(self):        
        self.uiUpdate.invokeAddCategoryUi(self.categorylistWidget)              
        self.updateUI()

    def removeCategory(self):
        itemName =  self.categorylistWidget.currentItem().text()
        itemRow =  max(0,(self.categorylistWidget.currentRow()-1))        
        self.categorylistWidget.setCurrentRow(itemRow)
        self.uiUpdate.removeCategory(itemName)
        self.categorylistWidget.clear()
        self.uiUpdate.uiInit(self.categorylistWidget,itemRow)
        self.updateUI()


    def assetContextMenu(self,point):
        self.popMenu = QMenu(self)
        self.actionAdd = QAction('Add',self, triggered=self.addAsset) 
        self.popMenu.addAction(self.actionAdd)
        self.actionEdit = QAction('Edit',self, triggered=self.editAsset) 
        self.popMenu.addAction(self.actionEdit)
        self.actionRemove = QAction('Remove',self, triggered=self.removeAsset) 
        self.popMenu.addAction(self.actionRemove)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/add.png"), QIcon.Normal, QIcon.Off)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/icons/remove.png"), QIcon.Normal, QIcon.Off)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/icons/edit.png"), QIcon.Normal, QIcon.Off)
        self.actionAdd.setIcon(icon)
        self.actionRemove.setIcon(icon1)
        self.actionEdit.setIcon(icon3) 

        self.popMenu.addSeparator()
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/icons/openData.png"), QIcon.Normal, QIcon.Off)
        self.actionOpen = QAction('open', self,triggered =  self.openAsset)
        self.popMenu.addAction(self.actionOpen)  
        self.actionOpen.setIcon(icon4)
        
        self.popMenu.addSeparator()
        self.actionExport = QAction('Export', self,triggered =  self.exportAsset)
        self.popMenu.addAction(self.actionExport)  
        self.popMenu.exec_(self.assetlistWidget.mapToGlobal(point))


    def addAsset(self):        
        self.uiUpdate.invokeAddAssetUI(self.categorylistWidget.currentRow(),self.assetlistWidget,None,None,None)


     


    def editAsset(self):      
        categoryName =  self.categorylistWidget.currentItem().text()
        itemName =  self.assetlistWidget.currentItem().text()
        self.uiUpdate.invokeAddAssetUI(self.categorylistWidget.currentRow(),self.assetlistWidget,True,categoryName,itemName)

    def removeAsset(self):
        category =  self.categorylistWidget.currentItem().text()
        itemName =  self.assetlistWidget.currentItem().text()
        self.uiUpdate.removeCategoryItem(category,itemName)
        self.updateUI()

    def exportAsset(self):
        print 'I will Export seet to Engine'

    def openAsset(self):
        categoryName =  self.categorylistWidget.currentItem().text()
        itemName =  self.assetlistWidget.currentItem().text()
        print abUtil.jDataH.jObj[categoryName][itemName]['filePath']

        








        
        
        




app =  QApplication(sys.argv)
form =  mainWindow()
form.show()
app.exec_()
