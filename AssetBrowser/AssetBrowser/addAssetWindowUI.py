# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\user\atri\AssetBrowser\AssetBrowser\AssetBrowser\UI\addAssetWindow.ui'
#
# Created: Wed Aug 16 22:12:23 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_addAssetWindow(object):
    def setupUi(self, addAssetWindow):
        addAssetWindow.setObjectName("addAssetWindow")
        addAssetWindow.resize(345, 160)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addAssetWindow.sizePolicy().hasHeightForWidth())
        addAssetWindow.setSizePolicy(sizePolicy)
        addAssetWindow.setMinimumSize(QtCore.QSize(345, 160))
        addAssetWindow.setMaximumSize(QtCore.QSize(345, 160))
        self.centralWidget = QtGui.QWidget(addAssetWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.widget = QtGui.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 345, 150))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 11, 316, 128))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.categoryLabel = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryLabel.sizePolicy().hasHeightForWidth())
        self.categoryLabel.setSizePolicy(sizePolicy)
        self.categoryLabel.setMinimumSize(QtCore.QSize(50, 25))
        self.categoryLabel.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.categoryLabel.setFont(font)
        self.categoryLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.categoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.categoryLabel.setObjectName("categoryLabel")
        self.horizontalLayout.addWidget(self.categoryLabel)
        self.categoryComboBox = QtGui.QComboBox(self.layoutWidget)
        self.categoryComboBox.setMinimumSize(QtCore.QSize(225, 25))
        self.categoryComboBox.setMaximumSize(QtCore.QSize(225, 25))
        self.categoryComboBox.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.horizontalLayout.addWidget(self.categoryComboBox)
        self.categoryAddButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.categoryAddButton.sizePolicy().hasHeightForWidth())
        self.categoryAddButton.setSizePolicy(sizePolicy)
        self.categoryAddButton.setMinimumSize(QtCore.QSize(25, 25))
        self.categoryAddButton.setMaximumSize(QtCore.QSize(25, 25))
        self.categoryAddButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Admin/Desktop/Testcons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.categoryAddButton.setIcon(icon)
        self.categoryAddButton.setObjectName("categoryAddButton")
        self.horizontalLayout.addWidget(self.categoryAddButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameLabel = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setMinimumSize(QtCore.QSize(50, 25))
        self.nameLabel.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_2.addWidget(self.nameLabel)
        self.assetNamelineEdit = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetNamelineEdit.sizePolicy().hasHeightForWidth())
        self.assetNamelineEdit.setSizePolicy(sizePolicy)
        self.assetNamelineEdit.setMinimumSize(QtCore.QSize(255, 25))
        self.assetNamelineEdit.setMaximumSize(QtCore.QSize(250, 25))
        self.assetNamelineEdit.setObjectName("assetNamelineEdit")
        self.horizontalLayout_2.addWidget(self.assetNamelineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pathLabel = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathLabel.sizePolicy().hasHeightForWidth())
        self.pathLabel.setSizePolicy(sizePolicy)
        self.pathLabel.setMinimumSize(QtCore.QSize(50, 25))
        self.pathLabel.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.pathLabel.setFont(font)
        self.pathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pathLabel.setObjectName("pathLabel")
        self.horizontalLayout_3.addWidget(self.pathLabel)
        self.assetPathlineEdit = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetPathlineEdit.sizePolicy().hasHeightForWidth())
        self.assetPathlineEdit.setSizePolicy(sizePolicy)
        self.assetPathlineEdit.setMinimumSize(QtCore.QSize(225, 25))
        self.assetPathlineEdit.setMaximumSize(QtCore.QSize(225, 25))
        self.assetPathlineEdit.setObjectName("assetPathlineEdit")
        self.horizontalLayout_3.addWidget(self.assetPathlineEdit)
        self.assetPathButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetPathButton.sizePolicy().hasHeightForWidth())
        self.assetPathButton.setSizePolicy(sizePolicy)
        self.assetPathButton.setMinimumSize(QtCore.QSize(25, 25))
        self.assetPathButton.setMaximumSize(QtCore.QSize(25, 25))
        self.assetPathButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/openData.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assetPathButton.setIcon(icon1)
        self.assetPathButton.setObjectName("assetPathButton")
        self.horizontalLayout_3.addWidget(self.assetPathButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imageLabel = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QtCore.QSize(50, 25))
        self.imageLabel.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.imageLabel.setFont(font)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout_4.addWidget(self.imageLabel)
        self.ssetPathlineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ssetPathlineEdit_2.sizePolicy().hasHeightForWidth())
        self.ssetPathlineEdit_2.setSizePolicy(sizePolicy)
        self.ssetPathlineEdit_2.setMinimumSize(QtCore.QSize(225, 25))
        self.ssetPathlineEdit_2.setMaximumSize(QtCore.QSize(225, 25))
        self.ssetPathlineEdit_2.setObjectName("ssetPathlineEdit_2")
        self.horizontalLayout_4.addWidget(self.ssetPathlineEdit_2)
        self.assetImageButton = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assetImageButton.sizePolicy().hasHeightForWidth())
        self.assetImageButton.setSizePolicy(sizePolicy)
        self.assetImageButton.setMinimumSize(QtCore.QSize(25, 25))
        self.assetImageButton.setMaximumSize(QtCore.QSize(25, 25))
        self.assetImageButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.assetImageButton.setIcon(icon2)
        self.assetImageButton.setObjectName("assetImageButton")
        self.horizontalLayout_4.addWidget(self.assetImageButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        addAssetWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(addAssetWindow)
        self.statusBar.setObjectName("statusBar")
        addAssetWindow.setStatusBar(self.statusBar)

        self.retranslateUi(addAssetWindow)
        QtCore.QMetaObject.connectSlotsByName(addAssetWindow)

    def retranslateUi(self, addAssetWindow):
        addAssetWindow.setWindowTitle(QtGui.QApplication.translate("addAssetWindow", "addAssetWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.categoryLabel.setText(QtGui.QApplication.translate("addAssetWindow", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("addAssetWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.pathLabel.setText(QtGui.QApplication.translate("addAssetWindow", "Path", None, QtGui.QApplication.UnicodeUTF8))
        self.imageLabel.setText(QtGui.QApplication.translate("addAssetWindow", "Image", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
