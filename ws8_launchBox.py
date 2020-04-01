from moudle import ws8basic
from ui.login import Ui_MainWindow
from ui.main import Ui_ws8Main
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QFileInfo)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import sys
import os
import subprocess

class loginBox(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(loginBox, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.pushButton.clicked.connect(self.logFunc)

    def logFunc(self):
        results = ws8basic.logIn(self.username.text(), self.passwd.text(), self.host.text())
        if results[1] == 0 :
            QMessageBox.information(self, "greet", results[0])
            self.close()
            self.mainW = mainWindowT()
            self.mainW.show()
        else:
            QMessageBox.information(self, "Error", results[0])

class mainWindowT(QMainWindow, Ui_ws8Main):
    def __init__(self, parent=None):
        super(mainWindowT, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.curUser.setText(ws8basic.getUser()['last_name'])
        self.getProjects = ws8basic.getProject4User()
        self.projectSelect.addItems(list(self.getProjects.keys()))
        self.projectSelect.itemClicked.connect(self.getSeqView)
        self.projectSelect.itemClicked.connect(self.getAssetView)
        self.projectSelect.itemClicked.connect(self.getRefView)
        self.seqView.itemClicked.connect(self.getTaskView)
        self.assetTree.doubleClicked.connect(self.openAssetFile)
        self.refTree.doubleClicked.connect(self.openRefFile)
        self.listWidget_CMP.itemDoubleClicked.connect(self.openComp)
        self.listWidget_FX.itemDoubleClicked.connect(self.openFx)
        #self.listWidget_LGT.itemDoubleClicked.connect(self.openLgt)
        #self.listWidget_MOD
        
    def getSeqView(self, item):
        self.seqView.clear()
        self.selProject = item.text()
        projectId = self.getProjects[self.selProject]
        getSequs = ws8basic.getSeq(projectId)
        sequsList = list(getSequs.keys())
        for seq in sequsList :
            seqID = getSequs[seq]
            seqItem = QTreeWidgetItem(self.seqView)
            seqItem.setText(0, seq)
            shotDict = ws8basic.getShot4User(seqID)
            shotList = list(shotDict.keys())
            for shot in shotList :
                shotitem = QTreeWidgetItem(seqItem)
                shotitem.setText(0, shot)

    def getAssetView(self, item):
        project = item.text()
        path = ws8basic.getAssets(project, 'assets')
        self.assetTreeModel = QFileSystemModel()
        self.assetTreeModel.setRootPath(path)
        self.assetTree.setModel(self.assetTreeModel)
        self.assetTree.setRootIndex(self.assetTreeModel.index(path))

    def getRefView(self, item):
        project = item.text()
        path = ws8basic.getAssets(project, 'reference')
        self.refTreeModel = QFileSystemModel()
        self.refTreeModel.setRootPath(path)
        self.refTree.setModel(self.refTreeModel)
        self.refTree.setRootIndex(self.refTreeModel.index(path))

    def getTaskView(self,item):
        self.listWidget_CMP.clear()
        self.listWidget_FX.clear()
        self.listWidget_LGT.clear()
        self.listWidget_MOD.clear()
        self.shotName = item.text(0)
        shotEle = self.shotName.split('_')
        taskType = ['CMP', 'LGT', 'MOD', 'FX']
        try:
            taskDict = ws8basic.getTaskDict(taskType, shotEle)
            self.listWidget_CMP.addItems(taskDict['CMP_task'])
            self.listWidget_FX.addItems(taskDict['FX_task'])
            self.listWidget_LGT.addItems(taskDict['LGT_task'])
            self.listWidget_MOD.addItems(taskDict['MOD_task'])
        except:
            pass

    def openAssetFile(self, index):
        indexItem = self.assetTreeModel.index(index.row(), 0, index.parent())
        filePath = self.assetTreeModel.filePath(indexItem)
        os.startfile(filePath)
        
    def openRefFile(self, index):
        indexItem = self.refTreeModel.index(index.row(), 0, index.parent())
        filePath = self.refTreeModel.filePath(indexItem)
        os.startfile(filePath)

    def openComp(self, item):
        self.compTask = item.text()
        path = f'd:/project/{self.selProject}/shot/{self.shotName}/CMP/task/{self.compTask}'
        nukeEXE = 'C:/Program Files/Nuke12.1v1/Nuke12.1.exe --nukex ' + path
        subprocess.Popen(nukeEXE)
        print(self.selProject)

    def openFx(self, item):
        self.fxTask = item.text()
        path = f'd:/project/{self.selProject}/shot/{self.shotName}/FX/task/{self.fxTask}'
        houExe = 'c:/Program Files/'
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    app.setStyle(QStyleFactory.create('Fusion'))
    
    login = loginBox()

    login.show()

    app.exec_()