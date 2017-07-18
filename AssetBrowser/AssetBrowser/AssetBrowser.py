from PySide.QtCore import *
from PySide.QtGui import *
import sys
import AssetBrowserUI
import assetBrowserUtil as abUtil





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
   






app =  QApplication(sys.argv)
form =  mainWindow()
form.show()
app.exec_()
