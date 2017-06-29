from PySide.QtCore import *
from PySide.QtGui import *
import sys
import AssetBrowserUI
import assetBrowserUtil



class mainWindow(QMainWindow,AssetBrowserUI.Ui_AssetBrowser):
    def __init__(self, parent =None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        categories = assetBrowserUtil.getCategory(assetBrowserUtil.readJson(assetBrowserUtil.jFile))
        self.categorylistWidget.addItems(categories)



app =  QApplication(sys.argv)
form =  mainWindow()



form.show()
app.exec_()
