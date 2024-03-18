# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import logo
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction,  QMessageBox


class Mainui(QtWidgets.QMainWindow):
    def setupUi(self):
        self.setMinimumSize(1000, 500)
        self.setWindowIcon(QIcon(':logo.png'))

        self.center()

        self.resize(762, 475)
        self.setAutoFillBackground(True)
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_log = QtWidgets.QLabel(self.centralwidget)
        self.label_log.setObjectName("label_log")
        self.horizontalLayout.addWidget(self.label_log)
        self.input_log = QtWidgets.QLineEdit(self.centralwidget)
        self.input_log.setMouseTracking(False)
        self.input_log.setReadOnly(True)
        self.input_log.setObjectName("input_log")
        self.horizontalLayout.addWidget(self.input_log)
        self.label_csv = QtWidgets.QLabel(self.centralwidget)
        self.label_csv.setMinimumSize(QtCore.QSize(0, 0))
        self.label_csv.setObjectName("label_csv")
        self.horizontalLayout.addWidget(self.label_csv)
        self.input_csv = QtWidgets.QLineEdit(self.centralwidget)
        self.input_csv.setReadOnly(True)
        self.input_csv.setObjectName("input_csv")
        self.horizontalLayout.addWidget(self.input_csv)
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setObjectName("label_img")
        self.horizontalLayout.addWidget(self.label_img)
        self.input_img = QtWidgets.QLineEdit(self.centralwidget)
        self.input_img.setReadOnly(True)
        self.input_img.setObjectName("input_img")
        self.horizontalLayout.addWidget(self.input_img)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.input_result = QtWidgets.QLineEdit(self.centralwidget)
        self.input_result.setReadOnly(True)
        self.input_result.setObjectName("input_result")
        self.horizontalLayout.addWidget(self.input_result)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setDisabled(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("color:skyblue;")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:skyblue;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.verticalLayout_3.addWidget(self.tableView_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:skyblue;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.tableView_3 = QtWidgets.QTableView(self.centralwidget)
        self.verticalLayout_4.addWidget(self.tableView_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.setMenuBar(self.menubar)
        self.action_Log = QtWidgets.QAction(self)
        self.action_Log.setObjectName("action_Log")
        self.action = QtWidgets.QAction(self)
        self.action.setObjectName("action")
        self.action_CSV = QtWidgets.QAction(self)
        self.action_CSV.setObjectName("action_CSV")
        self.action_3 = QtWidgets.QAction(self)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_Log)
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_CSV)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        # sys tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(':logo.png'))
        showAction = QAction("打开", self, triggered = self.Show)
        quitAction = QAction("退出", self, triggered = QCoreApplication.instance().quit)
        self.trayMenu = QMenu(self)
        self.trayMenu.addAction(showAction)
        self.trayMenu.addSeparator()
        self.trayMenu.addAction(quitAction)
        self.tray.setContextMenu(self.trayMenu)
        self.tray.show()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        self.move(int((screen.width() - window_size.width()) / 2) , int((screen.height() - window_size.height()) / 2))
    
    def Show(self):
        self.showNormal()
        self.activateWindow()
        self.setWindowFlags(QtCore.Qt.Window)
        self.center()
        self.show()

    def closeEvent(self, event): # 重写关闭事件
        reply = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("确定要退出吗?"), QMessageBox.NoButton, self)
        yr_btn = reply.addButton(self.tr("是的我要退出"), QMessageBox.YesRole)
        reply.addButton(self.tr("最小化到托盘"), QMessageBox.NoRole)
        reply.exec_()
        if reply.clickedButton() == yr_btn:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()
            self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint) # 最小化到托盘

    def retranslateUi(self, LogAnalysisTool):
        _translate = QtCore.QCoreApplication.translate
        LogAnalysisTool.setWindowTitle(_translate("LogAnalysisTool", "MainWindow"))
        self.label_log.setText(_translate("LogAnalysisTool", "Log 目录："))
        self.label_csv.setText(_translate("LogAnalysisTool", "CSV 目录："))
        self.label_img.setText(_translate("LogAnalysisTool", "图片目录："))
        self.label.setText(_translate("LogAnalysisTool", "结果保存目录："))
        self.pushButton.setText(_translate("LogAnalysisTool", "保存结果"))
        self.label_2.setText(_translate("LogAnalysisTool", "clean_result(0)"))
        self.label_3.setText(_translate("LogAnalysisTool", "send rcc"))
        self.label_4.setText(_translate("LogAnalysisTool", "same"))
        self.menu.setTitle(_translate("LogAnalysisTool", "文件"))
        self.action_Log.setText(_translate("LogAnalysisTool", "打开 Log 所在目录"))
        self.action_Log.setShortcut(_translate("LogAnalysisTool", "Ctrl+O"))
        self.action.setText(_translate("LogAnalysisTool", "设置结果保存目录"))
        # self.action.setShortcut(_translate("LogAnalysisTool", "Ctrl+S"))
        self.action_CSV.setText(_translate("LogAnalysisTool", "打开 CSV 所在目录"))
        self.action_3.setText(_translate("LogAnalysisTool", "打开 图片 所在目录"))
