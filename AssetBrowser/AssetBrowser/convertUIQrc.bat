@echo off
echo I will convert ui and qrc file for you
PAUSE
C:\Python27\Scripts\pyside-uic.exe E:\user\atri\AssetBrowser\AssetBrowser\AssetBrowser\UI\AssetBrowser.ui -o E:\user\atri\AssetBrowser\AssetBrowser\AssetBrowser\AssetBrowserUI.py
C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe E:\user\atri\AssetBrowser\AssetBrowser\AssetBrowser\icons.qrc -o E:\user\atri\AssetBrowser\AssetBrowser\AssetBrowser\icons_rc.py
echo All files has been converted goodbye
PAUSE