import io
import re
from decimal import Decimal

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QFileDialog

import aPhyloGeo.Alignement
import aPhyloGeo.aPhyloGeo
import folium
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from help import UiHowToUse
from parameters import UiDialog


class UiMainWindow(object):

    # added code from her[

    def useWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UiHowToUse()
        self.ui.setupUi(self.window)
        self.window.show()

    def paramWin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UiDialog()
        self.ui.setupUi(self.window)
        self.window.show()

    # open cl tree window
    def openWindow(self):
        from cltree import Ui_ct
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ct()
        self.ui.setupUi(self.window)
        self.window.show()

    def enableButton(self):
        if self.textEdit_4.toPlainText():
            self.pushButton_4.setEnabled(True)

    # to her]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1143, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1143, 670))
        MainWindow.setMaximumSize(QtCore.QSize(1143, 670))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/other/sherbrooke.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(0, -1, 1151, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(250, 250, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 163, 163))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 122, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(222, 221, 218))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.top_frame.setPalette(palette)
        self.top_frame.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_frame.setObjectName("top_frame")
        #
        self.pushButton_11 = QtWidgets.QPushButton(self.top_frame, clicked=lambda: self.useWindow())
        #
        self.pushButton_11.setGeometry(QtCore.QRect(1040, 10, 111, 81))
        self.pushButton_11.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../img/other/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.top_frame)  # button to access climatic section
        self.pushButton_3.setGeometry(QtCore.QRect(580, 10, 81, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../img/inactive/climatic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(75, 75))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(self.top_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 291, 81))
        #
        self.pushButton_3.clicked.connect(self.changeIconAndShowPage2)
        #
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../img/other/aPhylogeo.svg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.top_frame)  # button to access the results section
        self.pushButton_4.setGeometry(QtCore.QRect(770, 10, 81, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../img/disabled/result.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.top_frame)  # button to access genetic section
        self.pushButton_2.setGeometry(QtCore.QRect(380, 10, 101, 81))
        #
        self.pushButton_4.clicked.connect(self.changeIconAndShowPage3)
        self.pushButton_4.setEnabled(False)
        #
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../img/active/genetic.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QtCore.QSize(75, 75))
        #
        self.pushButton_2.clicked.connect(self.changeIconAndShowPage)
        self.pushButton_2.clicked.connect(self.enableFrame)
        #
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget = QtWidgets.QStackedWidget(
            self.centralwidget)  # stackedwidgets are the frames that appear only when the user
        self.stackedWidget.setGeometry(
            QtCore.QRect(0, 99, 1151, 581))  # clicks to generate something from a climatic or genetic file
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)  # e.g. sequence alignment, statistics, map, etc.
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(10, 0, 171, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)  # button to initiate sequence alignment
        self.pushButton_12.setGeometry(QtCore.QRect(10, 230, 61, 71))
        self.pushButton_12.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../img/disabled/sequence.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_12.setIcon(icon5)
        #
        self.pushButton_12.setEnabled(False)
        #
        self.pushButton_12.setIconSize(QtCore.QSize(60, 70))
        #
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 340, 71, 71))
        self.pushButton_13.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../img/disabled/statistics.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_13.setFlat(True)
        #
        self.pushButton_13.setEnabled(False)
        #
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 101, 41))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 240, 81, 51))
        self.label_5.setObjectName("label_5")
        #
        self.pushButton_6 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.pressIt())
        #
        self.pushButton_6.setGeometry(QtCore.QRect(0, 20, 71, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../img/other/Browse.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        #
        self.pushButton_7 = QtWidgets.QPushButton(self.frame,
                                                  clicked=lambda: self.clearIt())  # button to clear genetic file previously loaded
        #
        self.pushButton_7.setGeometry(QtCore.QRect(0, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../img/other/erase.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(80, 370, 67, 17))
        self.label_7.setObjectName("label_7")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(-10, 450, 91, 91))
        self.pushButton_16.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../img/disabled/tree.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_16.setIcon(icon9)
        self.pushButton_16.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_16.setFlat(True)
        #
        self.pushButton_16.setEnabled(False)
        #
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(70, 460, 91, 81))
        self.label_11.setObjectName("label_11")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(170, 0, 971, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEd_3 = QtWidgets.QTextEdit(self.frame_2)
        self.textEd_3.setGeometry(QtCore.QRect(30, 280, 931, 251))
        self.textEd_3.setObjectName("textEd_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_2)  # box where genetic file is loaded
        self.textEdit_4.setGeometry(QtCore.QRect(30, 10, 931, 531))
        self.textEdit_4.setObjectName("textEdit_4")
        #
        self.textEdit_4.textChanged.connect(self.onTextChanged)
        self.textEdit_4.textChanged.connect(self.onTextChangeGen)
        self.textEdit_4.setReadOnly(True)
        #
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_3 = QtWidgets.QFrame(self.page_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 0, 171, 551))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        # self.pushButton_14 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 230, 61, 71))
        self.pushButton_14.setText("")
        #
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../img/inactive/sequence.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #
        self.pushButton_14.setIcon(icon10)
        self.pushButton_14.setIconSize(QtCore.QSize(60, 70))
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_15.setGeometry(QtCore.QRect(0, 340, 71, 71))
        self.pushButton_15.setText("")
        #
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../img/inactive/statistics.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #
        self.pushButton_15.setIcon(icon11)
        self.pushButton_15.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_15.setFlat(True)
        #
        self.pushButton_15.clicked.connect(self.showGenStatFrame4)
        self.pushButton_15.clicked.connect(self.enableFrame4)
        #
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(70, 40, 101, 41))
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(80, 240, 81, 51))
        self.label_8.setObjectName("label_8")
        #
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3, clicked=lambda: self.pressIt())
        self.pushButton_8.clicked.connect(self.changeIconAndShowPage)
        self.pushButton_8.clicked.connect(self.enableFrame)
        #
        # self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setGeometry(QtCore.QRect(0, 20, 71, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        # self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
        #
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3,
                                                  clicked=lambda: self.clearGenStat())  # button to clear genetic statistics
        self.pushButton_9.clicked.connect(self.resetCom2)
        #
        self.pushButton_9.setGeometry(QtCore.QRect(0, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(70, 140, 101, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(80, 370, 67, 17))
        self.label_10.setObjectName("label_10")
        self.label_37 = QtWidgets.QLabel(self.frame_3)
        self.label_37.setGeometry(QtCore.QRect(70, 460, 91, 81))
        self.label_37.setObjectName("label_37")
        self.pushButton_34 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_34.setGeometry(QtCore.QRect(-10, 450, 91, 91))
        self.pushButton_34.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../img/inactive/tree.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_34.setIcon(icon12)
        self.pushButton_34.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_34.setFlat(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setGeometry(QtCore.QRect(170, 0, 971, 551))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_4)  # box where genetic stats should appear
        self.textBrowser.setGeometry(QtCore.QRect(20, 70, 941, 441))
        self.textBrowser.setObjectName("textBrowser")
        self.back = QtWidgets.QPushButton(self.frame_4)
        self.back.setGeometry(QtCore.QRect(860, 520, 89, 25))
        self.back.setObjectName("back")
        self.label = QtWidgets.QLabel(self.frame_4)
        #
        self.back.clicked.connect(self.showPage)
        self.back.clicked.connect(self.enableFrame)
        #
        self.label.setGeometry(QtCore.QRect(640, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_4)  # dialog box to select species for genetic stats
        self.comboBox_2.setGeometry(QtCore.QRect(760, 30, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setFrame(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_38 = QtWidgets.QLabel(self.frame_4)
        self.label_38.setGeometry(QtCore.QRect(400, 20, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.frame_5 = QtWidgets.QFrame(self.page_3)
        self.frame_5.setGeometry(QtCore.QRect(10, 0, 171, 551))
        self.frame_5.setBaseSize(QtCore.QSize(0, 0))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_17.setGeometry(QtCore.QRect(10, 230, 61, 71))
        self.pushButton_17.setText("")
        self.pushButton_17.setIcon(icon10)
        self.pushButton_17.setIconSize(QtCore.QSize(60, 70))
        self.pushButton_17.setFlat(True)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_18.setGeometry(QtCore.QRect(0, 340, 71, 71))
        self.pushButton_18.setText("")
        self.pushButton_18.setIcon(icon11)
        self.pushButton_18.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_18.setFlat(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setGeometry(QtCore.QRect(70, 40, 101, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setGeometry(QtCore.QRect(80, 240, 81, 51))
        self.label_13.setObjectName("label_13")
        #
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_5, clicked=lambda: self.pressIt())
        self.pushButton_10.clicked.connect(self.changeIconAndShowPage)
        self.pushButton_10.clicked.connect(self.enableFrame)
        #
        # self.pushButton_10 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 20, 71, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon7)
        self.pushButton_10.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        #
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_5, clicked=lambda: self.clearGenTree())
        #
        # self.pushButton_19 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_19.setGeometry(QtCore.QRect(0, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon8)
        self.pushButton_19.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_19.setCheckable(False)
        self.pushButton_19.setFlat(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(70, 140, 101, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(80, 370, 67, 17))
        self.label_15.setObjectName("label_15")
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_20.setGeometry(QtCore.QRect(-10, 450, 91, 91))
        self.pushButton_20.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../img/inactive/tree.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_20.setIcon(icon13)
        self.pushButton_20.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_20.setFlat(True)
        self.pushButton_20.setObjectName("pushButton_20")
        self.label_16 = QtWidgets.QLabel(self.frame_5)
        self.label_16.setGeometry(QtCore.QRect(70, 460, 91, 81))
        self.label_16.setObjectName("label_16")
        self.frame_6 = QtWidgets.QFrame(self.page_3)
        self.frame_6.setGeometry(QtCore.QRect(180, 0, 971, 551))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_17 = QtWidgets.QLabel(self.frame_6)
        self.label_17.setGeometry(QtCore.QRect(390, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_6)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 50, 941, 461))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.back_2 = QtWidgets.QPushButton(self.frame_6)
        #
        self.back_2.clicked.connect(self.showPage)
        #
        self.back_2.setGeometry(QtCore.QRect(870, 520, 89, 25))
        self.back_2.setObjectName("back_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.frame_7 = QtWidgets.QFrame(self.page_4)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 181, 551))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        #
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_7, clicked=lambda: self.clearCl())
        #
        self.pushButton_21.setGeometry(QtCore.QRect(10, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon8)
        self.pushButton_21.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_21.setCheckable(False)
        self.pushButton_21.setFlat(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_7, clicked=lambda: self.openWindow())
        self.pushButton_22.setGeometry(QtCore.QRect(0, 350, 91, 91))
        self.pushButton_22.setText("")
        self.pushButton_22.setIcon(icon9)
        self.pushButton_22.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_22.setFlat(True)
        #
        self.pushButton_22.setEnabled(False)
        self.pushButton_22.clicked.connect(self.showClimTreeFrame13)
        self.pushButton_22.clicked.connect(self.enableFrame13)
        #
        self.pushButton_22.setObjectName("pushButton_22")
        #
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_7, clicked=lambda: self.pressit())
        #
        self.pushButton_23.setGeometry(QtCore.QRect(0, 20, 91, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setText("")
        self.pushButton_23.setIcon(icon7)
        self.pushButton_23.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_23.setCheckable(False)
        self.pushButton_23.setFlat(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.label_18 = QtWidgets.QLabel(self.frame_7)
        self.label_18.setGeometry(QtCore.QRect(80, 40, 111, 41))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_7)
        self.label_19.setGeometry(QtCore.QRect(80, 360, 91, 81))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_7)
        self.label_20.setGeometry(QtCore.QRect(80, 140, 101, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setGeometry(QtCore.QRect(90, 270, 67, 17))
        self.label_21.setObjectName("label_21")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_7,
                                                   clicked=lambda: self.showClimStatBar())  # button to show climatic stats
        self.pushButton_24.setGeometry(QtCore.QRect(10, 240, 71, 71))
        self.pushButton_24.setText("")
        self.pushButton_24.setIcon(icon6)
        self.pushButton_24.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_24.setFlat(True)
        #
        self.pushButton_24.setEnabled(False)
        self.pushButton_24.clicked.connect(self.showClimStatFrame10)
        self.pushButton_24.clicked.connect(self.enableFrame10)
        #
        self.pushButton_24.setObjectName("pushButton_24")
        self.frame_8 = QtWidgets.QFrame(self.page_4)
        self.frame_8.setGeometry(QtCore.QRect(180, 0, 961, 541))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_8)  # box where climatic data is loaded
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 20, 931, 231))
        self.textBrowser_3.setObjectName("textBrowser_3")
        #
        self.textBrowser_3.textChanged.connect(self.onTextChanged)
        self.textBrowser_3.textChanged.connect(self.onTextChangeClim)
        #
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_8)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 280, 931, 251))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_9 = QtWidgets.QFrame(self.page_5)
        self.frame_9.setGeometry(QtCore.QRect(0, 0, 181, 551))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        #
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_9, clicked=lambda: self.clearClimStat())
        self.pushButton_25.clicked.connect(self.resetCom)
        #
        # self.pushButton_25 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setText("")
        self.pushButton_25.setIcon(icon8)
        self.pushButton_25.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_25.setCheckable(False)
        self.pushButton_25.setFlat(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_26.setGeometry(QtCore.QRect(0, 350, 91, 91))
        self.pushButton_26.setText("")
        self.pushButton_26.setIcon(icon13)
        self.pushButton_26.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_26.setFlat(True)
        self.pushButton_26.setObjectName("pushButton_26")
        #
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_9, clicked=lambda: self.pressit())
        self.pushButton_27.clicked.connect(self.showPage4)
        #
        # self.pushButton_27 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_27.setGeometry(QtCore.QRect(0, 20, 91, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setText("")
        self.pushButton_27.setIcon(icon7)
        self.pushButton_27.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_27.setCheckable(False)
        self.pushButton_27.setFlat(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_22 = QtWidgets.QLabel(self.frame_9)
        self.label_22.setGeometry(QtCore.QRect(80, 40, 111, 41))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_9)
        self.label_23.setGeometry(QtCore.QRect(80, 360, 91, 81))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_9)
        self.label_24.setGeometry(QtCore.QRect(80, 140, 101, 31))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_9)
        self.label_25.setGeometry(QtCore.QRect(90, 270, 67, 17))
        self.label_25.setObjectName("label_25")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_28.setGeometry(QtCore.QRect(10, 240, 71, 71))
        self.pushButton_28.setText("")
        self.pushButton_28.setIcon(icon11)
        self.pushButton_28.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_28.setFlat(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.frame_10 = QtWidgets.QFrame(self.page_5)
        self.frame_10.setGeometry(QtCore.QRect(180, 0, 961, 551))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_11 = QtWidgets.QFrame(self.frame_10)
        self.frame_11.setGeometry(QtCore.QRect(580, 30, 411, 51))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.comboBox_3 = QtWidgets.QComboBox(
            self.frame_11)  # dialog box to choose climate condition for climatic graph
        self.comboBox_3.setGeometry(QtCore.QRect(160, 20, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setFrame(True)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_26 = QtWidgets.QLabel(self.frame_11)
        self.label_26.setGeometry(QtCore.QRect(20, 20, 141, 31))
        self.label_26.setObjectName("label_26")
        self.comboBox = QtWidgets.QComboBox(self.frame_10)  # dialog box to choose a type of graph for climatic data
        self.comboBox.setGeometry(QtCore.QRect(110, 50, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_27 = QtWidgets.QLabel(self.frame_10)
        self.label_27.setGeometry(QtCore.QRect(20, 50, 81, 31))
        self.label_27.setObjectName("label_27")
        self.textBrowser_4 = QtWidgets.QTextBrowser(
            self.frame_10)  # Box where climatic stats appear. Maybe remove since graph
        self.textBrowser_4.setGeometry(
            QtCore.QRect(20, 90, 921, 421))  # from matplotlib is rendered in a separate window
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.back_3 = QtWidgets.QPushButton(self.frame_10)
        #
        self.back_3.clicked.connect(self.showPage4)
        self.back_3.clicked.connect(self.enableFrame)
        #
        self.back_3.setGeometry(QtCore.QRect(830, 520, 89, 25))
        self.back_3.setObjectName("back_3")
        self.label_39 = QtWidgets.QLabel(self.frame_10)
        self.label_39.setGeometry(QtCore.QRect(400, 20, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frame_12 = QtWidgets.QFrame(self.page_6)
        self.frame_12.setGeometry(QtCore.QRect(0, 0, 181, 551))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        #
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_12, clicked=lambda: self.clearClimTree())
        #
        # self.pushButton_29 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_29.setGeometry(QtCore.QRect(10, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setText("")
        self.pushButton_29.setIcon(icon8)
        self.pushButton_29.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_29.setCheckable(False)
        self.pushButton_29.setFlat(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_30.setGeometry(QtCore.QRect(0, 350, 91, 91))
        self.pushButton_30.setText("")
        self.pushButton_30.setIcon(icon13)
        self.pushButton_30.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_30.setFlat(True)
        self.pushButton_30.setObjectName("pushButton_30")
        #
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_12, clicked=lambda: self.pressit())
        self.pushButton_31.clicked.connect(self.showPage4)
        #
        # self.pushButton_31 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_31.setGeometry(QtCore.QRect(0, 20, 91, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setText("")
        self.pushButton_31.setIcon(icon7)
        self.pushButton_31.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_31.setCheckable(False)
        self.pushButton_31.setFlat(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.label_28 = QtWidgets.QLabel(self.frame_12)
        self.label_28.setGeometry(QtCore.QRect(80, 40, 111, 41))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_12)
        self.label_29.setGeometry(QtCore.QRect(80, 360, 91, 81))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_12)
        self.label_30.setGeometry(QtCore.QRect(80, 140, 101, 31))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_12)
        self.label_31.setGeometry(QtCore.QRect(90, 270, 67, 17))
        self.label_31.setObjectName("label_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_32.setGeometry(QtCore.QRect(10, 240, 71, 71))
        self.pushButton_32.setText("")
        self.pushButton_32.setIcon(icon11)
        self.pushButton_32.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_32.setFlat(True)
        self.pushButton_32.setObjectName("pushButton_32")
        self.frame_13 = QtWidgets.QFrame(self.page_6)
        self.frame_13.setGeometry(QtCore.QRect(180, 0, 961, 551))
        self.frame_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame_13)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 40, 941, 471))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_32 = QtWidgets.QLabel(self.frame_13)
        self.label_32.setGeometry(QtCore.QRect(370, 10, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.back_4 = QtWidgets.QPushButton(self.frame_13)
        #
        self.back_4.clicked.connect(self.showPage4)
        self.back_4.clicked.connect(self.enableFrame)
        #
        self.back_4.setGeometry(QtCore.QRect(830, 520, 89, 25))
        self.back_4.setObjectName("back_4")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_14 = QtWidgets.QFrame(self.page_7)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 181, 551))
        self.frame_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        #
        self.pushButton = QtWidgets.QPushButton(self.frame_14, clicked=lambda: self.paramWin())
        #
        self.pushButton.setGeometry(QtCore.QRect(0, 40, 81, 61))
        self.pushButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../img/inactive/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_33 = QtWidgets.QPushButton(self.frame_14,
                                                   clicked=lambda: self.showFilteredResults())  # submit button to show the final results
        self.pushButton_33.setGeometry(QtCore.QRect(10, 230, 71, 61))
        self.pushButton_33.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../img/inactive/submit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_33.setIcon(icon15)
        self.pushButton_33.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_33.setFlat(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.label_33 = QtWidgets.QLabel(self.frame_14)
        self.label_33.setGeometry(QtCore.QRect(90, 60, 81, 31))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_14)
        self.label_34.setGeometry(QtCore.QRect(90, 240, 67, 21))
        self.label_34.setObjectName("label_34")
        self.label_40 = QtWidgets.QLabel(self.frame_14)
        self.label_40.setGeometry(QtCore.QRect(90, 350, 67, 17))
        self.label_40.setObjectName("label_40")
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_14)
        #
        self.pushButton_35.clicked.connect(self.showResultStatFrame16)
        self.pushButton_35.clicked.connect(self.enableFrame17)
        #
        self.pushButton_35.setGeometry(QtCore.QRect(10, 320, 71, 71))
        self.pushButton_35.setText("")
        self.pushButton_35.setIcon(icon11)
        self.pushButton_35.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_35.setFlat(True)
        self.pushButton_35.setObjectName("pushButton_35")
        self.label_52 = QtWidgets.QLabel(self.frame_14)
        self.label_52.setGeometry(QtCore.QRect(90, 150, 101, 31))
        self.label_52.setObjectName("label_52")
        #
        self.pushButton_43 = QtWidgets.QPushButton(self.frame_14, clicked=lambda: self.clearResult())
        #
        self.pushButton_43.setGeometry(QtCore.QRect(10, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setText("")
        self.pushButton_43.setIcon(icon8)
        self.pushButton_43.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_43.setCheckable(False)
        self.pushButton_43.setFlat(True)
        self.pushButton_43.setObjectName("pushButton_43")
        self.frame_15 = QtWidgets.QFrame(self.page_7)
        self.frame_15.setGeometry(QtCore.QRect(180, 0, 951, 561))
        self.frame_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.frame_15)
        self.textBrowser_7.setGeometry(QtCore.QRect(10, 40, 931, 491))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_36 = QtWidgets.QLabel(self.frame_15)
        self.label_36.setGeometry(QtCore.QRect(400, 10, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.frame_16 = QtWidgets.QFrame(self.page_8)
        self.frame_16.setGeometry(QtCore.QRect(0, 0, 181, 551))
        self.frame_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        #
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_16, clicked=lambda: self.paramWin())
        self.pushButton_5.clicked.connect(self.changeIconAndShowPage3)
        #
        self.pushButton_5.setGeometry(QtCore.QRect(0, 40, 81, 61))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon14)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_36.setGeometry(QtCore.QRect(10, 230, 71, 61))
        self.pushButton_36.setText("")
        self.pushButton_36.setIcon(icon15)
        self.pushButton_36.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_36.setFlat(True)
        self.pushButton_36.setObjectName("pushButton_36")
        self.label_41 = QtWidgets.QLabel(self.frame_16)
        self.label_41.setGeometry(QtCore.QRect(90, 60, 81, 31))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_16)
        self.label_42.setGeometry(QtCore.QRect(90, 240, 67, 21))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_16)
        self.label_43.setGeometry(QtCore.QRect(90, 350, 67, 17))
        self.label_43.setObjectName("label_43")
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_37.setGeometry(QtCore.QRect(10, 320, 71, 71))
        self.pushButton_37.setText("")
        self.pushButton_37.setIcon(icon11)
        self.pushButton_37.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_37.setFlat(True)
        self.pushButton_37.setObjectName("pushButton_37")
        self.label_53 = QtWidgets.QLabel(self.frame_16)
        self.label_53.setGeometry(QtCore.QRect(90, 150, 101, 31))
        self.label_53.setObjectName("label_53")
        #
        self.pushButton_44 = QtWidgets.QPushButton(self.frame_16, clicked=lambda: self.clearResultStat())
        self.pushButton_44.clicked.connect(self.resetCom_4_5)
        #
        self.pushButton_44.setGeometry(QtCore.QRect(10, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setText("")
        self.pushButton_44.setIcon(icon8)
        self.pushButton_44.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_44.setCheckable(False)
        self.pushButton_44.setFlat(True)
        self.pushButton_44.setObjectName("pushButton_44")
        self.frame_17 = QtWidgets.QFrame(self.page_8)
        self.frame_17.setGeometry(QtCore.QRect(180, 0, 961, 571))
        self.frame_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.frame_17)
        self.textBrowser_6.setGeometry(QtCore.QRect(10, 70, 941, 441))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.back_5 = QtWidgets.QPushButton(self.frame_17)
        #
        self.back_5.clicked.connect(self.showPage7)
        #
        self.back_5.setGeometry(QtCore.QRect(860, 520, 89, 25))
        self.back_5.setObjectName("back_5")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_17)
        self.comboBox_4.setGeometry(QtCore.QRect(110, 30, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setFrame(True)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_44 = QtWidgets.QLabel(self.frame_17)
        self.label_44.setGeometry(QtCore.QRect(650, 30, 91, 31))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_17)
        self.label_45.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.label_45.setObjectName("label_45")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_17)
        self.comboBox_5.setGeometry(QtCore.QRect(750, 30, 201, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setFrame(True)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_51 = QtWidgets.QLabel(self.frame_17)
        self.label_51.setGeometry(QtCore.QRect(400, 20, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.frame_18 = QtWidgets.QFrame(self.page_9)
        self.frame_18.setGeometry(QtCore.QRect(10, 0, 171, 561))
        self.frame_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_38.setGeometry(QtCore.QRect(10, 230, 61, 71))
        self.pushButton_38.setText("")
        #
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../img/inactive/sequence.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #
        self.pushButton_38.setIcon(icon10)
        self.pushButton_38.setIconSize(QtCore.QSize(60, 70))
        self.pushButton_38.setFlat(True)
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_39.setGeometry(QtCore.QRect(0, 340, 71, 71))
        self.pushButton_39.setText("")
        #
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../img/inactive/sequence.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #
        self.pushButton_39.setIcon(icon11)
        self.pushButton_39.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_39.setFlat(True)
        self.pushButton_39.setObjectName("pushButton_39")
        self.label_35 = QtWidgets.QLabel(self.frame_18)
        self.label_35.setGeometry(QtCore.QRect(70, 40, 101, 41))
        self.label_35.setObjectName("label_35")
        self.label_46 = QtWidgets.QLabel(self.frame_18)
        self.label_46.setGeometry(QtCore.QRect(80, 240, 71, 51))
        self.label_46.setObjectName("label_46")
        #
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_18, clicked=lambda: self.pressIt())
        self.pushButton_40.clicked.connect(self.changeIconAndShowPage)
        self.pushButton_40.clicked.connect(self.enableFrame)
        #
        self.pushButton_40.setGeometry(QtCore.QRect(0, 20, 71, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setText("")
        self.pushButton_40.setIcon(icon7)
        self.pushButton_40.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_40.setCheckable(False)
        self.pushButton_40.setFlat(True)
        self.pushButton_40.setObjectName("pushButton_40")
        #
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_18, clicked=lambda: self.clearSeq())
        #
        self.pushButton_41.setGeometry(QtCore.QRect(0, 120, 61, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setText("")
        self.pushButton_41.setIcon(icon8)
        self.pushButton_41.setIconSize(QtCore.QSize(60, 90))
        self.pushButton_41.setCheckable(False)
        self.pushButton_41.setFlat(True)
        self.pushButton_41.setObjectName("pushButton_41")
        self.label_47 = QtWidgets.QLabel(self.frame_18)
        self.label_47.setGeometry(QtCore.QRect(70, 140, 101, 31))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.frame_18)
        self.label_48.setGeometry(QtCore.QRect(80, 370, 67, 17))
        self.label_48.setObjectName("label_48")
        self.pushButton_42 = QtWidgets.QPushButton(self.frame_18)
        self.pushButton_42.setGeometry(QtCore.QRect(-10, 450, 91, 91))
        self.pushButton_42.setText("")
        self.pushButton_42.setIcon(icon13)
        self.pushButton_42.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_42.setFlat(True)
        self.pushButton_42.setObjectName("pushButton_42")
        self.label_49 = QtWidgets.QLabel(self.frame_18)
        self.label_49.setGeometry(QtCore.QRect(70, 460, 91, 81))
        self.label_49.setObjectName("label_49")
        self.frame_19 = QtWidgets.QFrame(self.page_9)
        self.frame_19.setGeometry(QtCore.QRect(180, 0, 971, 571))
        self.frame_19.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.textEd_4 = QtWidgets.QTextEdit(self.frame_19)
        self.textEd_4.setGeometry(QtCore.QRect(10, 60, 941, 451))
        self.textEd_4.setObjectName("textEd_4")
        self.label_50 = QtWidgets.QLabel(self.frame_19)
        self.label_50.setGeometry(QtCore.QRect(360, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.back_6 = QtWidgets.QPushButton(self.frame_19)
        self.back_6.setGeometry(QtCore.QRect(850, 520, 89, 25))
        self.back_6.setObjectName("back_6")
        #
        self.back_6.clicked.connect(self.showPage)
        self.back_6.clicked.connect(self.enableFrame)
        #
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.stackedWidget.addWidget(self.page_15)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.translateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_2.clicked.connect(self.showPage)
        self.pushButton_3.clicked.connect(self.showPage4)
        self.pushButton_4.clicked.connect(self.showPage7)
        self.pushButton_12.clicked.connect(self.showSeqAlinFrame19)
        self.pushButton_14.clicked.connect(self.showSeqAlinFrame19)
        self.pushButton_17.clicked.connect(self.showSeqAlinFrame19)
        self.pushButton_13.clicked.connect(self.showGenStatFrame4)
        self.pushButton_18.clicked.connect(self.showGenStatFrame4)
        self.pushButton_39.clicked.connect(self.showGenStatFrame4)
        self.pushButton_16.clicked.connect(self.showGenTreeFrame6)
        self.pushButton_34.clicked.connect(self.showGenTreeFrame6)
        self.pushButton_42.clicked.connect(self.showGenTreeFrame6)
        self.pushButton_26.clicked.connect(self.showClimTreeFrame13)
        self.pushButton_24.clicked.connect(self.showClimStatFrame10)
        self.pushButton_32.clicked.connect(self.showClimStatFrame10)
        self.pushButton_35.clicked.connect(self.showResultStatFrame16)

        buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                   self.pushButton_6, self.pushButton_7, self.pushButton_8,
                   self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12, self.pushButton_13,
                   self.pushButton_14, self.pushButton_15, self.pushButton_16,
                   self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20, self.pushButton_21,
                   self.pushButton_22, self.pushButton_23, self.pushButton_24,
                   self.pushButton_25, self.pushButton_26, self.pushButton_27, self.pushButton_28, self.pushButton_29,
                   self.pushButton_30, self.pushButton_31, self.pushButton_32,
                   self.pushButton_33, self.pushButton_34, self.pushButton_35, self.pushButton_35, self.pushButton_36,
                   self.pushButton_37, self.pushButton_38,
                   self.pushButton_39, self.pushButton_40, self.pushButton_41, self.pushButton_42, self.pushButton_43,
                   self.pushButton_44, self.back,

                   ]

        # Set slider and stylesheet for all buttons
        for button in buttons:
            button.setCursor(Qt.PointingHandCursor)
            button.setStyleSheet("""
            QPushButton:hover {
            background-color: grey;
            color: white;
            border: none;
            padding: 20px;
            border-radius: 10px;
            font-size: 13px;
            }
            """)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.currentIndexChanged.connect(self.showFrame)
        self.frame_11.setHidden(True)

    def pressIt(self):
        '''
        Retrieve data from genetic file and show it in color
        '''
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None, "Select FASTA file", "", " (*.fasta);; (*.fasta)",
                                                  options=options)
        if fileName:
            aPhyloGeo.Alignement.userData_align.set_referenceGeneFile(fileName)
            with open(fileName, "r") as f:
                self.clearIt()
                content = f.read()
                self.textEdit_4.setText(content)
                sequence = ""
                for line in content.splitlines():
                    if not line.startswith('>'):
                        new_line = ''
                        for char in line:
                            if char == 'A':
                                new_line += f'<span style="background-color: yellow">{char}</span>'
                            elif char == 'C':
                                new_line += f'<span style="background-color: blue">{char}</span>'
                            elif char == 'G':
                                new_line += f'<span style="background-color: red">{char}</span>'
                            elif char == 'T':
                                new_line += f'<span style="background-color: orange">{char}</span>'
                        line = new_line
                    sequence += line + "<br>"
                self.textEdit_4.setText(sequence)

    def callSeqAlign(self):
        '''
        Initiate sequence alignment
        Return: genetic dictionary used for the final filter
        '''
        if self.textEd_4.toPlainText() == "":
            align_obj = aPhyloGeo.Alignement.AlignSequences()
            seq_al = align_obj.aligned
            obj = str(seq_al)
            self.textEd_4.setText(obj)
            self.genTree = aPhyloGeo.aPhyloGeo.createGenTree(align_obj)
        return self.genTree

    def retrieveDataNames(self, list):
        '''
        Retrieve data from a list, except for first element
        Args: 
         list (from which we get data)
        Return: 
         names_to_retrieve (Retrieved elements)
        '''
        names_to_retrieve = []
        for data in list:
            if data != list[0]:
                names_to_retrieve.append(data)
        return names_to_retrieve

    def populateMap(self, lat, long):
        '''
        Create folium map
        Args:
         lat (latitude), long (longitude)
        '''
        mean_lat = 0
        mean_long = 0
        for y in lat:
            mean_lat = mean_lat + Decimal(y)
        mean_lat = mean_lat / len(lat)
        for x in long:
            mean_long = mean_long + Decimal(x)
        mean_long = mean_long / len(long)
        m = folium.Map(location=[mean_lat, mean_long],
                       zoom_start=14,
                       tiles="OpenStreetMap")
        i = 0
        while i < len(lat):
            folium.Marker([Decimal(lat[i]), Decimal(long[i])]).add_to(m)
            i = i + 1
        # m.save('m.html')                  #folium map does not appear correctly on MAC with webbrowser.open(),
        # web browser.open('m.html')         #but it does not appear correctly on Linux with webview.show()
        # will have to be fixed
        data = io.BytesIO()
        m.save(data, close_file=False)
        self.webview = QWebEngineView()
        self.webview.setWindowTitle("Climate Map")
        self.webview.setHtml(data.getvalue().decode())
        self.webview.show()

    def pressit(self):
        '''
        Retrieve data from climatic file and show it in a table
        If the last 2 columns of the data are 'LAT' and 'LONG',
        generate a folium map with these columns
        '''
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None, "Select CSV file", "", "Comma Separated Values (*.csv)",
                                                  options=options)

        if fileName:
            aPhyloGeo.aPhyloGeo.userData.set_fileName(fileName)
            with open(fileName, "r") as c:
                lines = c.readlines()
                num_rows = len(lines)
                first_line = lines[0].split(",")
                lat = []
                long = []
                self.species = []
                self.factors = [[], [], [], [], []]
                loc = False
                num_columns = len(first_line)
                if first_line[len(first_line) - 2] == 'LAT':
                    first_line_without_loc = first_line
                    first_line_without_loc.pop(len(first_line_without_loc) - 1)
                    first_line_without_loc.pop(len(first_line_without_loc) - 1)
                    clim_data_names = self.retrieveDataNames(first_line_without_loc)
                    aPhyloGeo.aPhyloGeo.userData.set_names(first_line_without_loc)
                    aPhyloGeo.Alignement.userData_align.set_names(first_line_without_loc)
                    loc = True
                else:
                    clim_data_names = self.retrieveDataNames(first_line)
                    aPhyloGeo.aPhyloGeo.userData.set_names(first_line)
                    aPhyloGeo.Alignement.userData_align.set_names(first_line)
                aPhyloGeo.aPhyloGeo.userData.set_dataNames(clim_data_names)
                aPhyloGeo.Alignement.userData_align.set_dataNames(clim_data_names)
                self.textBrowser_3.clear()
                cursor = QtGui.QTextCursor(self.textBrowser_3.textCursor())
                clim_data_table = cursor.insertTable(num_rows, num_columns)
                fmt = clim_data_table.format()
                fmt.setWidth(QtGui.QTextLength(QtGui.QTextLength.PercentageLength, 100))
                clim_data_table.setFormat(fmt)
                format = QtGui.QTextCharFormat()
                format.setForeground(QtGui.QColor('#006400'))
                i = 0
                for line in lines:
                    line_split = line.split(",")
                    if line != lines[0] and loc == True:
                        lat.append(line_split[len(line_split) - 2])
                        long.append(line_split[len(line_split) - 1])
                        self.species.append(line_split[0])
                        for j in [1, 2, 3, 4, 5]:
                            self.factors[i].append(line_split[j])
                        i += 1
                    if line != lines[0] and loc == False:
                        self.species.append(line_split[0])
                        for j in [1, 2, 3, 4, 5]:
                            self.factors[i].append(line_split[j])
                        i += 1
                    for value in line_split:
                        if line == lines[0]:
                            cursor.setCharFormat(format)
                        if re.search("^[0-9\\-]*\\.[0-9]*", value) is not None:
                            cursor.insertText(str(round(Decimal(value), 3)))
                            cursor.movePosition(QtGui.QTextCursor.NextCell)
                        else:
                            cursor.insertText(value)
                            cursor.movePosition(QtGui.QTextCursor.NextCell)
                if loc == True:
                    self.populateMap(lat, long)
                self.child_window = QtWidgets.QMainWindow()
                self.ui = UiHowToUse()
                self.ui.setupUi(self.child_window)
                self.child_window.setWindowModality(QtCore.Qt.NonModal)

    def showClimStatBar(self):
        # Condition should be added to show plot
        # according to user choice
        self.showClimStatBarAllFact()

    def showClimStatBarAllFact(self):
        '''
        Generate a bar graph that includes every factor for every species
        '''
        self.factors[0] = [float(v) for v in self.factors[0]]
        self.factors[1] = [float(v) for v in self.factors[1]]
        self.factors[2] = [float(v) for v in self.factors[2]]
        self.factors[3] = [float(v) for v in self.factors[3]]
        self.factors[4] = [float(v) for v in self.factors[4]]

        barWidth = 0.15
        fig = plt.subplots(figsize=(15, 10))
        br1 = np.arange(len(self.factors[0]))
        br2 = [x + barWidth for x in br1]
        br3 = [x + barWidth for x in br2]
        br4 = [x + barWidth for x in br3]
        br5 = [x + barWidth for x in br4]
        plt.bar(br1, self.factors[0], color='black', width=barWidth,
                edgecolor='grey', label=self.species[0])
        plt.bar(br2, self.factors[1], color='red', width=barWidth,
                edgecolor='grey', label=self.species[1])
        plt.bar(br3, self.factors[2], color='green', width=barWidth,
                edgecolor='grey', label=self.species[2])
        plt.bar(br4, self.factors[3], color='blue', width=barWidth,
                edgecolor='grey', label=self.species[3])
        plt.bar(br5, self.factors[4], color='cyan', width=barWidth,
                edgecolor='grey', label=self.species[4])
        plt.xlabel('COVID-19 Variant', fontweight='bold')
        plt.ylabel("Climatic data", fontweight='bold')
        plt.xticks([r + barWidth for r in range(len(self.factors[0]))],
                   aPhyloGeo.aPhyloGeo.userData.get_dataNames())
        plt.yticks(np.arange(0, 30))
        plt.title("Distribution of climatic variables for each COVID Variant")
        plt.legend()
        plt.show()

    def showFrame(self, value):
        if value is not None:
            self.frame_11.setHidden(False)
        else:
            self.frame_11.setHidden(True)

    def showPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def showGenStatFrame4(self):
        self.stackedWidget.setCurrentIndex(1)

    def showGenTreeFrame6(self):
        self.stackedWidget.setCurrentIndex(2)

    def showPage4(self):
        self.stackedWidget.setCurrentIndex(3)

    def showClimStatFrame10(self):
        self.stackedWidget.setCurrentIndex(4)

    def showClimTreeFrame13(self):
        self.stackedWidget.setCurrentIndex(5)

    def showPage7(self):
        self.stackedWidget.setCurrentIndex(6)

    def showResultStatFrame16(self):
        self.stackedWidget.setCurrentIndex(7)

    def showSeqAlinFrame19(self):
        self.geneticTreeDict = self.callSeqAlign()
        self.stackedWidget.setCurrentIndex(8)

    def showFilteredResults(self):
        '''
        Show the results filtered with a metric threshold provided by user
        '''
        aPhyloGeo.aPhyloGeo.filterResults(
            aPhyloGeo.aPhyloGeo.climaticPipeline(aPhyloGeo.aPhyloGeo.userData.get_fileName(),
                                                 aPhyloGeo.aPhyloGeo.userData.get_names()),
            self.geneticTreeDict)
        with open("output.csv", "r") as f:
            content = f.read()
        self.textBrowser_7.setText(str(content))

    # Enable_button():
    def onTextChanged(self):
        if self.textEdit_4.toPlainText() and self.textBrowser_3.toPlainText():
            self.pushButton_4.setEnabled(True)
            self.pushButton_4.setIcon(QIcon("../img/inactive/result.svg"))
        else:
            self.pushButton_4.setEnabled(False)

    def onTextChangeGen(self):
        if self.textEdit_4.toPlainText():
            self.pushButton_12.setEnabled(True)
            self.pushButton_13.setEnabled(True)
            self.pushButton_16.setEnabled(True)
            self.pushButton_12.setIcon(QIcon("../img/inactive/sequence.svg"))
            self.pushButton_13.setIcon(QIcon("../img/inactive/statistics.svg"))
            self.pushButton_16.setIcon(QIcon("../img/inactive/tree.svg"))

        else:
            self.pushButton_12.setEnabled(False)
            self.pushButton_13.setEnabled(False)
            self.pushButton_16.setEnabled(False)

    def onTextChangeClim(self):
        if self.textBrowser_3.toPlainText():
            self.pushButton_24.setEnabled(True)
            self.pushButton_22.setEnabled(True)
            self.pushButton_24.setIcon(QIcon("../img/inactive/statistics.svg"))
            self.pushButton_22.setIcon(QIcon("../img/inactive/tree.svg"))

        else:
            self.pushButton_24.setEnabled(False)
            self.pushButton_22.setEnabled(False)

    # enable the frame when the push button is clicked
    def enableFrame(self):
        self.frame_2.setEnabled(True)
        self.frame.setEnabled(True)

    def enableFrame8(self):
        self.frame_8.setEnabled(False)
        self.frame_7.setEnabled(False)

    def enableFrame4(self):
        self.frame_4.setEnabled(True)
        self.showGenStatFrame4()

    def enableFrame10(self):
        self.frame_10.setEnabled(True)
        self.showGenStatFrame4()

    def enableFrame13(self):
        self.frame_13.setEnabled(True)
        # self.showGenStatFrame4()

    def enableFrame17(self):
        self.frame_17.setEnabled(True)

    def changeIconAndShowPage2(self):
        if self.pushButton_3.icon().isNull():
            self.pushButton_3.setIcon(QIcon("icon2.png"))
        else:
            self.pushButton_3.setIcon(QIcon("../img/active/climatic.svg"))
            self.pushButton_2.setIcon(QIcon("../img/inactive/genetic.svg"))
            self.pushButton_4.setIcon(QIcon("../img/inactive/result.svg"))
        self.showPage4()

    def changeIconAndShowPage(self):
        if self.pushButton_2.icon().isNull():
            self.pushButton_2.setIcon(QIcon("icon1.png"))
        else:
            self.pushButton_3.setIcon(QIcon("../img/inactive/climatic.svg"))
            self.pushButton_2.setIcon(QIcon("../img/active/genetic.svg"))
            self.pushButton_4.setIcon(QIcon("../img/inactive/result.svg"))
        self.showPage()

    def changeIconAndShowPage3(self):
        if self.pushButton_4.icon().isNull():
            self.pushButton_4.setIcon(QIcon("icon3.png"))
        else:
            self.pushButton_3.setIcon(QIcon("../img/inactive/climatic.svg"))
            self.pushButton_2.setIcon(QIcon("../img/inactive/genetic.svg"))
            self.pushButton_4.setIcon(QIcon("../img/active/result.svg"))
        self.showPage7()

    # press the button to delete data
    def clearIt(self):
        self.textEd_4.clear()
        self.textEdit_4.clear()

    def clearSeq(self):
        self.textEd_4.clear()

    def clearGenStat(self):
        self.textBrowser.clear()

    def clearGenTree(self):
        self.textBrowser_2.clear()

    def clearCl(self):
        self.textBrowser_3.clear()

    def clearClimStat(self):
        self.textBrowser_4.clear()

    def clearClimTree(self):
        self.textBrowser_5.clear()

    def clearResult(self):
        self.textBrowser_7.clear()
        # tableView

    def clearResultStat(self):
        self.textBrowser_6.clear()
        # graphicsView_4

    # Set the combo box to its default value
    def resetCom2(self):
        self.comboBox_2.setCurrentIndex(0)
        # reset_button.clicked.connect(self.resetCom2resetCom2)

    def resetCom(self):
        self.comboBox.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)

    def resetCom_4_5(self):
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)

    def translateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_11.setToolTip(_translate("MainWindow", "How to use the application"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "Climatic Data"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "Results"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "Genetic Data"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "Down"))
        self.label_2.setText(_translate("MainWindow", "File Browser"))
        self.label_5.setText(_translate("MainWindow", " Sequence \n"
                                                      "Alignment"))
        self.label_3.setText(_translate("MainWindow", "Clear"))
        self.label_7.setText(_translate("MainWindow", "Statistics"))
        self.label_11.setText(_translate("MainWindow", "Genetic Tree"))
        self.label_4.setText(_translate("MainWindow", "File Browser"))
        self.label_8.setText(_translate("MainWindow", " Sequence \n"
                                                      "Alignment"))
        self.label_9.setText(_translate("MainWindow", "Clear"))
        self.label_10.setText(_translate("MainWindow", "Statistics"))
        self.label_37.setText(_translate("MainWindow", "Genetic Tree"))
        self.back.setText(_translate("MainWindow", "back"))
        self.label.setText(_translate("MainWindow", "Species name"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "species1"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "species2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "species3"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "species4"))
        self.label_38.setText(_translate("MainWindow", "Statistics"))
        self.label_12.setText(_translate("MainWindow", "File Browser"))
        self.label_13.setText(_translate("MainWindow", " Sequence \n"
                                                       "Alignment"))
        self.label_14.setText(_translate("MainWindow", "Clear"))
        self.label_15.setText(_translate("MainWindow", "Statistics"))
        self.label_16.setText(_translate("MainWindow", "Genetic Tree"))
        self.label_17.setText(_translate("MainWindow", "Genetic Tree"))
        self.back_2.setText(_translate("MainWindow", "back"))
        self.label_18.setText(_translate("MainWindow", "File Browser"))
        self.label_19.setText(_translate("MainWindow", "Climatic Tree"))
        self.label_20.setText(_translate("MainWindow", "Clear"))
        self.label_21.setText(_translate("MainWindow", "Statistics"))
        self.label_22.setText(_translate("MainWindow", "File Browser"))
        self.label_23.setText(_translate("MainWindow", "Climatic Tree"))
        self.label_24.setText(_translate("MainWindow", "Clear"))
        self.label_25.setText(_translate("MainWindow", "Statistics"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Temperature"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Wind"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Humidity"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Altitude"))
        self.label_26.setText(_translate("MainWindow", "  Climate condition"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Bar Chart"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Line Chart"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Pie Chart"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Area Chart"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Scatter Chart"))
        self.label_27.setText(_translate("MainWindow", "Chart Type "))
        self.back_3.setText(_translate("MainWindow", "back"))
        self.label_39.setText(_translate("MainWindow", "Statistics"))
        self.label_28.setText(_translate("MainWindow", "File Browser"))
        self.label_29.setText(_translate("MainWindow", "Climatic Tree"))
        self.label_30.setText(_translate("MainWindow", "Clear"))
        self.label_31.setText(_translate("MainWindow", "Statistics"))
        self.label_32.setText(_translate("MainWindow", "Climatic Tree"))
        self.back_4.setText(_translate("MainWindow", "back"))
        self.label_33.setText(_translate("MainWindow", "Settings"))
        self.label_34.setText(_translate("MainWindow", "Submit"))
        self.label_40.setText(_translate("MainWindow", "Statistics"))
        self.label_52.setText(_translate("MainWindow", "Clear"))
        self.label_36.setText(_translate("MainWindow", "Result  "))
        self.label_41.setText(_translate("MainWindow", "Settings"))
        self.label_42.setText(_translate("MainWindow", "Submit"))
        self.label_43.setText(_translate("MainWindow", "Statistics"))
        self.label_53.setText(_translate("MainWindow", "Clear"))
        self.back_5.setText(_translate("MainWindow", "back"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Bar Chart"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Line Chart"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Pie Chart"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Area Chart"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "Scatter Chart"))
        self.label_44.setText(_translate("MainWindow", "   condition"))
        self.label_45.setText(_translate("MainWindow", "Chart Type "))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "All"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Temperature"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Wind"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Humidity"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Altitude"))
        self.label_51.setText(_translate("MainWindow", "Statistics"))
        self.label_35.setText(_translate("MainWindow", "File Browser"))
        self.label_46.setText(_translate("MainWindow", " Sequence \n"
                                                       "Alignment"))
        self.label_47.setText(_translate("MainWindow", "Clear"))
        self.label_48.setText(_translate("MainWindow", "Statistics"))
        self.label_49.setText(_translate("MainWindow", "Genetic Tree"))
        self.label_50.setText(_translate("MainWindow", "Sequence Alignment"))
        self.back_6.setText(_translate("MainWindow", "back"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
