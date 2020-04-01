# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_ui.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(301, 191)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(300, 150))
        self.centralwidget.setMaximumSize(QSize(300, 150))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")
        self.username.setMaxLength(50)
        self.username.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.username, 6, 0, 1, 1)

        self.host = QLineEdit(self.centralwidget)
        self.host.setObjectName(u"host")
        self.host.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.host, 5, 0, 1, 1)

        self.passwd = QLineEdit(self.centralwidget)
        self.passwd.setObjectName(u"passwd")
        self.passwd.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.passwd, 7, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMaximumSize(QSize(100, 100))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CrossCursor))
        self.pushButton.setFlat(False)

        self.gridLayout.addWidget(self.pushButton, 5, 2, 3, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(20, 10))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 301, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.pushButton.show)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"login", None))
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.host.setText(QCoreApplication.translate("MainWindow", u"kistu.workshop8.cn", None))
        self.host.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668", None))
        self.passwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Launch", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" workShop8 launchBox                                                         ", None))
    # retranslateUi

