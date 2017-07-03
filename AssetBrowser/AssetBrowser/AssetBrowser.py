from PySide.QtCore import *
from PySide.QtGui import *
import sys
import AssetBrowserUI
import assetBrowserUtil as autil
jDataH =  autil.jsonDataHandler()



class mainWindow(QMainWindow,AssetBrowserUI.Ui_AssetBrowser):
    def __init__(self, parent =None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.categories = jDataH.getCategory()
        self.categorylistWidget.addItems(self.categories)
        self.categorylistWidget.setCurrentRow(0)
        self.assetlistWidget.setViewMode(QListView.IconMode)
        autil.SetAssetTextIcon(self.assetlistWidget)




app =  QApplication(sys.argv)
form =  mainWindow()
form.show()
app.exec_()
