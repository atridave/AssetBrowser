from PySide.QtCore import *
from PySide.QtGui import *
import sys
import AssetBrowserUI
import assetBrowserUtil as abUtil




class mainWindow(QMainWindow,AssetBrowserUI.Ui_AssetBrowser):
    def __init__(self, parent =None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        abUtil.UiUpdate().uiInit(self.categorylistWidget)
        abUtil.UiUpdate().changeViewMode(self.assetlistWidget,1)
        itemName =  self.categorylistWidget.currentItem().text()
        itemRow =  self.categorylistWidget.currentRow()
        abUtil.UiUpdate().setItems(self.assetlistWidget,itemName)        
        self.categorylistWidget.itemClicked.connect(self.updateUI)
      

    def updateUI(self):
        print 'I will updateUI'        
        self.assetlistWidget.clear()
        itemName =  self.categorylistWidget.currentItem().text()
        abUtil.UiUpdate().setItems(self.assetlistWidget,itemName)
       


app =  QApplication(sys.argv)
form =  mainWindow()
form.show()
app.exec_()
