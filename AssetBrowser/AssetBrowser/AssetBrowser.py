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
        self.actionExport = QAction('Export', self,triggered =  self.exportAsset)
        self.popMenu.addAction(self.actionExport)  
        self.popMenu.exec_(self.assetlistWidget.mapToGlobal(point))

    #def createActions(self):
    #    self.addAsset = 'Print hello'

    def addAsset(self):
        print 'I will add asset for you'
        #import maya.cmds as cmds
        #cmds.polyCube()
    def editAsset(self):
        print 'I will Edit asset for you'

    def removeAsset(self):
        print 'I will remove asset for you'

    def exportAsset(self):
        print 'I will Export seet to Engine'
   






app =  QApplication(sys.argv)
form =  mainWindow()
form.show()
app.exec_()
