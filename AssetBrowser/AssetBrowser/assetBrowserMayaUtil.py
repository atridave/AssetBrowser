import maya._OpenMayaUI as oui
import shiboken
import maya.cmds as cmds
import os,fnmatch




def getMayaWindow():
    pointer =  oui.MQtUtil_mainWindow()
    return shiboken.wrapInstance(long(pointer),QWidget)


def makeThumbnil(filePath):
    path = maya.cmds.playblast(
        format="image",
        viewer=False,
        percent=100,
        quality=100,
        frame=1,
        width=400,
        height=400,
        filename=filePath,
        endTime=1,
        startTime=1,
        offScreen=0,
        forceOverwrite=True,
        showOrnaments=False,
        compression='png',
    )
    return path


#makeThumbnil('E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\assetIcons\\all_mus')

def makeFileIcons():

    path = 'E:\\myProjects\\ProjectAssets'
    iconFolderPath =  'E:\\user\\atri\\AssetBrowser\\AssetBrowser\\AssetBrowser\\assetIcons'

    serchFiles = [os.path.join(dirpath, f)
        for dirpath, dirnames, files in os.walk(path)
        for f in fnmatch.filter(files, '*.ma')]

    for i in range(0,len(serchFiles)):
        cmds.file(serchFiles[i],open = True,force=True)
        fileName =  (os.path.basename(serchFiles[i]).split('.ma'))[0]
        filePath =  os.path.join(iconFolderPath,fileName)
        imageName =   makeThumbnil(filePath)
        






