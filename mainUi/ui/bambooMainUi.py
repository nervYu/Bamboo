# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_Ui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_bambooMain(object):
    def setupUi(self, bambooMain):
        if bambooMain.objectName():
            bambooMain.setObjectName(u"bambooMain")
        bambooMain.resize(598, 586)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bambooMain.sizePolicy().hasHeightForWidth())
        bambooMain.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"C:/Users/Yutao/Desktop/\u516b\u53f7\u5de5\u574a_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        bambooMain.setWindowIcon(icon)
        bambooMain.setWindowOpacity(1.000000000000000)
        bambooMain.setStyleSheet(u"background-color: rgb(241, 241, 241);")
        bambooMain.setIconSize(QSize(60, 60))
        self.actionAbout = QAction(bambooMain)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(bambooMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.seqView = QTreeWidget(self.centralwidget)
        self.seqView.setObjectName(u"seqView")

        self.gridLayout.addWidget(self.seqView, 2, 1, 1, 1)

        self.tabArea01 = QTabWidget(self.centralwidget)
        self.tabArea01.setObjectName(u"tabArea01")
        self.assetTab = QWidget()
        self.assetTab.setObjectName(u"assetTab")
        self.assetTree = QTreeView(self.assetTab)
        self.assetTree.setObjectName(u"assetTree")
        self.assetTree.setGeometry(QRect(-2, -1, 511, 221))
        self.tabArea01.addTab(self.assetTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.refTree = QTreeView(self.tab)
        self.refTree.setObjectName(u"refTree")
        self.refTree.setGeometry(QRect(-2, -1, 511, 221))
        self.tabArea01.addTab(self.tab, "")
        self.toolTab = QWidget()
        self.toolTab.setObjectName(u"toolTab")
        self.horizontalLayout = QHBoxLayout(self.toolTab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabArea01.addTab(self.toolTab, "")

        self.gridLayout.addWidget(self.tabArea01, 1, 1, 1, 3)

        self.tabArea_Task = QTabWidget(self.centralwidget)
        self.tabArea_Task.setObjectName(u"tabArea_Task")
        font = QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.tabArea_Task.setFont(font)
        self.tab_FX = QWidget()
        self.tab_FX.setObjectName(u"tab_FX")
        self.listWidget_FX = QListWidget(self.tab_FX)
        self.listWidget_FX.setObjectName(u"listWidget_FX")
        self.listWidget_FX.setGeometry(QRect(-1, -1, 251, 231))
        self.listWidget_FX.setStyleSheet(u"border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tabArea_Task.addTab(self.tab_FX, "")
        self.tab_CMP = QWidget()
        self.tab_CMP.setObjectName(u"tab_CMP")
        self.listWidget_CMP = QListWidget(self.tab_CMP)
        self.listWidget_CMP.setObjectName(u"listWidget_CMP")
        self.listWidget_CMP.setGeometry(QRect(-1, -1, 261, 231))
        self.tabArea_Task.addTab(self.tab_CMP, "")
        self.tab_Lgt = QWidget()
        self.tab_Lgt.setObjectName(u"tab_Lgt")
        self.listWidget_LGT = QListWidget(self.tab_Lgt)
        self.listWidget_LGT.setObjectName(u"listWidget_LGT")
        self.listWidget_LGT.setGeometry(QRect(-1, -1, 250, 231))
        self.listWidget_LGT.setStyleSheet(u"border-top-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tabArea_Task.addTab(self.tab_Lgt, "")
        self.tab_MOD = QWidget()
        self.tab_MOD.setObjectName(u"tab_MOD")
        self.listWidget_MOD = QListWidget(self.tab_MOD)
        self.listWidget_MOD.setObjectName(u"listWidget_MOD")
        self.listWidget_MOD.setGeometry(QRect(-1, -1, 251, 241))
        self.tabArea_Task.addTab(self.tab_MOD, "")

        self.gridLayout.addWidget(self.tabArea_Task, 2, 3, 1, 1)

        self.curUser = QLabel(self.centralwidget)
        self.curUser.setObjectName(u"curUser")
        font1 = QFont()
        font1.setPointSize(16)
        self.curUser.setFont(font1)
        self.curUser.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.curUser, 0, 3, 1, 1)

        self.projectSelect = QListWidget(self.centralwidget)
        self.projectSelect.setObjectName(u"projectSelect")
        self.projectSelect.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.projectSelect, 1, 0, 2, 1)

        bambooMain.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(bambooMain)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 598, 21))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        bambooMain.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(bambooMain)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        bambooMain.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(bambooMain)

        self.tabArea01.setCurrentIndex(1)
        self.tabArea_Task.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(bambooMain)
    # setupUi

    def retranslateUi(self, bambooMain):
        bambooMain.setWindowTitle(QCoreApplication.translate("bambooMain", u"workshop8 LaunchBox", None))
        self.actionAbout.setText(QCoreApplication.translate("bambooMain", u"about", None))
        ___qtreewidgetitem = self.seqView.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("bambooMain", u"seqView", None));
        self.tabArea01.setTabText(self.tabArea01.indexOf(self.assetTab), QCoreApplication.translate("bambooMain", u"Asset", None))
        self.tabArea01.setTabText(self.tabArea01.indexOf(self.tab), QCoreApplication.translate("bambooMain", u"Reference", None))
        self.tabArea01.setTabText(self.tabArea01.indexOf(self.toolTab), QCoreApplication.translate("bambooMain", u"Tool", None))
        self.tabArea_Task.setTabText(self.tabArea_Task.indexOf(self.tab_FX), QCoreApplication.translate("bambooMain", u"FX", None))
        self.tabArea_Task.setTabText(self.tabArea_Task.indexOf(self.tab_CMP), QCoreApplication.translate("bambooMain", u"CMP", None))
        self.tabArea_Task.setTabText(self.tabArea_Task.indexOf(self.tab_Lgt), QCoreApplication.translate("bambooMain", u"LGT", None))
        self.tabArea_Task.setTabText(self.tabArea_Task.indexOf(self.tab_MOD), QCoreApplication.translate("bambooMain", u"MOD", None))
        self.curUser.setText(QCoreApplication.translate("bambooMain", u"TextLabel", None))
        self.menuAbout.setTitle(QCoreApplication.translate("bambooMain", u"about", None))
    # retranslateUi

