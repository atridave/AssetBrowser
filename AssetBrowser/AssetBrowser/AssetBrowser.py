from PySide.QtCore import *
from PySide.QtGui import *
import sys
import AssetBrowserUI


class mainWindow(QMainWindow,AssetBrowserUI.Ui_AssetBrowser):
    def __init__(self, parent =None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)


app =  QApplication(sys.argv)
form =  mainWindow()
form.show()
app.exec_()
