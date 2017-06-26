import maya._OpenMayaUI as oui
import shiboken
import maya.cmds as cmds

def getMayaWindow():
    pointer =  oui.MQtUtil_mainWindow()
    return shiboken.wrapInstance(long(pointer),QWidget)



