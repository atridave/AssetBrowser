import maya._OpenMayaUI as oui
import shiboken
import maya.cmds as cmds

def getMayaWindow():
    pointer =  oui.MQtUtil_mainWindow()
    return shiboken.wrapInstance(long(pointer),QWidget)



def makeThumbnil():
    path = maya.cmds.playblast(
        format="image",
        viewer=False,
        percent=100,
        quality=100,
        frame=1,
        width=200,
        height=200,
        filename='C:\\Users\\Admin\\Documents\\maya\\projects\\default\\images\\tmp\\aa',
        endTime=1,
        startTime=1,
        offScreen=0,
        forceOverwrite=True,
        showOrnaments=False,
        compression='png',
    )
    return path

