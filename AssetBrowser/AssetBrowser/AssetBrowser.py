from PySide.QtCore import *
from PySide.QtGui import *
import sys
import AssetBrowserUI
import assetBrowserUtil as abUtil





class mainWindow(QMainWindow,AssetBrowserUI.Ui_AssetBrowser):
    def __init__(self, parent =None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        abUtil.UiUpdate().uiInit(self.categorylistWidget,2)
        abUtil.UiUpdate().changeViewMode(self.assetlistWidget,1)
        itemName =  self.categorylistWidget.currentItem().text()
        #itemRow =  self.categorylistWidget.currentRow()
        abUtil.UiUpdate().setItems(self.assetlistWidget,itemName)        
        self.categorylistWidget.itemClicked.connect(self.updateUI)
        self.addButton.clicked.connect(self.addCategory)
        self.removeButton.clicked.connect(self.removeCategory)         
        
    

    def updateUI(self):
        self.assetlistWidget.clear()
        itemName =  self.categorylistWidget.currentItem().text()
        abUtil.UiUpdate().setItems(self.assetlistWidget,itemName)

    def addCategory(self):
        
        abUtil.UiUpdate().invokeAddCategoryUi(self.categorylistWidget)
        abUtil.UiUpdate().addCategory('NewObj')
        self.categorylistWidget.clear()
        abUtil.UiUpdate().uiInit(self.categorylistWidget)

        newItem = self.categorylistWidget.findItems('newObj',Qt.MatchContains)
        for item in newItem:
            itemRow = self.categorylistWidget.row(item)

        self.categorylistWidget.clear()
        abUtil.UiUpdate().uiInit(self.categorylistWidget,itemRow)        
        self.updateUI()

    def removeCategory(self):
        itemName =  self.categorylistWidget.currentItem().text()
        itemRow =  (self.categorylistWidget.currentRow()-1)
        self.categorylistWidget.setCurrentRow(itemRow)
        abUtil.UiUpdate().removeCategory(itemName)
        self.categorylistWidget.clear()
        abUtil.UiUpdate().uiInit(self.categorylistWidget,itemRow)
        self.updateUI()
   






app =  QApplication(sys.argv)
form =  mainWindow()
form.show()
app.exec_()
