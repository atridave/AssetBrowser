# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\user\atri\AssetBrowser\AssetBrowser\AssetBrowser\UI\addCategory.ui'
#
# Created: Wed Aug 16 22:12:22 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_addCategory(object):
    def setupUi(self, addCategory):
        addCategory.setObjectName("addCategory")
        addCategory.resize(184, 29)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addCategory.sizePolicy().hasHeightForWidth())
        addCategory.setSizePolicy(sizePolicy)
        addCategory.setMinimumSize(QtCore.QSize(175, 25))
        addCategory.setMaximumSize(QtCore.QSize(1000, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addCategory.setWindowIcon(icon)
        self.widget = QtGui.QWidget(addCategory)
        self.widget.setGeometry(QtCore.QRect(0, 0, 175, 25))
        self.widget.setObjectName("widget")
        self.addlineEdit = QtGui.QLineEdit(self.widget)
        self.addlineEdit.setGeometry(QtCore.QRect(0, 0, 150, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addlineEdit.sizePolicy().hasHeightForWidth())
        self.addlineEdit.setSizePolicy(sizePolicy)
        self.addlineEdit.setMinimumSize(QtCore.QSize(150, 25))
        self.addlineEdit.setMaximumSize(QtCore.QSize(150, 25))
        self.addlineEdit.setObjectName("addlineEdit")
        self.addButton = QtGui.QPushButton(self.widget)
        self.addButton.setGeometry(QtCore.QRect(150, 0, 25, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setMinimumSize(QtCore.QSize(25, 25))
        self.addButton.setMaximumSize(QtCore.QSize(1000, 1000))
        self.addButton.setText("")
        self.addButton.setIcon(icon)
        self.addButton.setObjectName("addButton")

        self.retranslateUi(addCategory)
        QtCore.QMetaObject.connectSlotsByName(addCategory)

    def retranslateUi(self, addCategory):
        addCategory.setWindowTitle(QtGui.QApplication.translate("addCategory", "addCategory", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
