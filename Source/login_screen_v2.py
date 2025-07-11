# Form implementation generated from reading ui file 'login_screen_v2.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1513, 747)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QStatusBar{\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"background:rgb(255, 255, 255)\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-50, -11, 1571, 331))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.widget_5.setGeometry(QtCore.QRect(330, 30, 120, 80))
        self.widget_5.setStyleSheet("QWidget {\n"
"    border: 5px solid rgb(75, 57, 239);\n"
"    border-radius: 0 0 0 10px;\n"
"}")
        self.widget_5.setObjectName("widget_5")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"border:0px;")
        self.label_5.setObjectName("label_5")
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.widget_6.setGeometry(QtCore.QRect(380, 70, 120, 80))
        self.widget_6.setStyleSheet("QWidget {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border: 5px solid  rgb(57, 210, 192);\n"
"    border-radius: 0 0 0 10px;\n"
"}\n"
"")
        self.widget_6.setObjectName("widget_6")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"border:0px;")
        self.label_6.setObjectName("label_6")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(-20, 160, 1541, 181))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 80px;\n"
"margin-bottom:0px;")
        self.widget_3.setObjectName("widget_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(710, 90, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_2.setGeometry(QtCore.QRect(570, 70, 120, 80))
        self.widget_2.setStyleSheet("QWidget {\n"
"    border: 5px solid rgb(75, 57, 239);\n"
"    border-radius: 0 0 0 10px;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:1px ;\n"
"color: rgb(0, 0, 0);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_3.setObjectName("label_3")
        self.widget_4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(-30, 270, 1551, 361))
        self.widget_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.widget_4.setObjectName("widget_4")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_2.setGeometry(QtCore.QRect(610, 210, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.widget_4)
        self.label.setGeometry(QtCore.QRect(610, 150, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_4)
        self.lineEdit.setGeometry(QtCore.QRect(716, 140, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(716, 210, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(716, 280, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {    background-color: rgb(75, 57, 239);\n"
"    color: white;\n"
"    border: none;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
" }\n"
"QPushButton:pressed {\n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"}\n"
"\n"
"")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.widget_13 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_13.setGeometry(QtCore.QRect(0, 660, 601, 80))
        self.widget_13.setStyleSheet("color: rgb(0, 0, 0);")
        self.widget_13.setObjectName("widget_13")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_13)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.widget_14 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_14.setGeometry(QtCore.QRect(970, 660, 601, 80))
        self.widget_14.setStyleSheet("color: rgb(0, 0, 0);")
        self.widget_14.setObjectName("widget_14")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_14)
        self.label_8.setGeometry(QtCore.QRect(310, 60, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.widget_10 = QtWidgets.QWidget(parent=self.widget_14)
        self.widget_10.setGeometry(QtCore.QRect(370, -60, 41, 21))
        self.widget_10.setStyleSheet("QWidget {\n"
"    border: 5px solid rgb(75, 57, 239);\n"
"    border-radius: 0 0 0 10px;\n"
"}")
        self.widget_10.setObjectName("widget_10")
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_14)
        self.widget_8.setGeometry(QtCore.QRect(460, -60, 31, 21))
        self.widget_8.setStyleSheet("QWidget {\n"
"    border: 5px solid rgb(75, 57, 239);\n"
"    border-radius: 0 0 0 10px;\n"
"}")
        self.widget_8.setObjectName("widget_8")
        self.widget_11 = QtWidgets.QWidget(parent=self.widget_14)
        self.widget_11.setGeometry(QtCore.QRect(430, -120, 41, 21))
        self.widget_11.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 5px solid  rgb(57, 210, 192);\n"
"    border-radius: 0 0 0 10px;\n"
"}\n"
"")
        self.widget_11.setObjectName("widget_11")
        self.widget_12 = QtWidgets.QWidget(parent=self.widget_14)
        self.widget_12.setGeometry(QtCore.QRect(390, -90, 51, 21))
        self.widget_12.setStyleSheet("QWidget {\n"
"    border: 5px solid rgb(75, 57, 239);\n"
"    border-radius: 0 0 0 10px;\n"
"}")
        self.widget_12.setObjectName("widget_12")
        self.widget_9 = QtWidgets.QWidget(parent=self.widget_14)
        self.widget_9.setGeometry(QtCore.QRect(420, -60, 31, 21))
        self.widget_9.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 5px solid  rgb(57, 210, 192);\n"
"    border-radius: 0 0 0 10px;\n"
"}\n"
"")
        self.widget_9.setObjectName("widget_9")
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_14)
        self.widget_7.setGeometry(QtCore.QRect(450, -90, 51, 21))
        self.widget_7.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 5px solid  rgb(57, 210, 192);\n"
"    border-radius: 0 0 0 10px;\n"
"}\n"
"")
        self.widget_7.setObjectName("widget_7")
        self.widget_15 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_15.setGeometry(QtCore.QRect(1360, 680, 41, 21))
        self.widget_15.setStyleSheet("QWidget {\n"
"    border: 5px solid rgb(75, 57, 239);\n"
"    border-radius: 0 0 0 10px;\n"
"}")
        self.widget_15.setObjectName("widget_15")
        self.widget_16 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_16.setGeometry(QtCore.QRect(1450, 680, 31, 21))
        self.widget_16.setStyleSheet("QWidget {\n"
"    border: 5px solid rgb(75, 57, 239);\n"
"    border-radius: 0 0 0 10px;\n"
"}")
        self.widget_16.setObjectName("widget_16")
        self.widget_17 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_17.setGeometry(QtCore.QRect(1420, 620, 41, 21))
        self.widget_17.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 5px solid  rgb(57, 210, 192);\n"
"    border-radius: 0 0 0 10px;\n"
"}\n"
"")
        self.widget_17.setObjectName("widget_17")
        self.widget_18 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_18.setGeometry(QtCore.QRect(1380, 650, 51, 21))
        self.widget_18.setStyleSheet("QWidget {\n"
"    border: 5px solid rgb(75, 57, 239);\n"
"    border-radius: 0 0 0 10px;\n"
"}")
        self.widget_18.setObjectName("widget_18")
        self.widget_19 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_19.setGeometry(QtCore.QRect(1410, 680, 31, 21))
        self.widget_19.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 5px solid  rgb(57, 210, 192);\n"
"    border-radius: 0 0 0 10px;\n"
"}\n"
"")
        self.widget_19.setObjectName("widget_19")
        self.widget_20 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_20.setGeometry(QtCore.QRect(1440, 650, 51, 21))
        self.widget_20.setStyleSheet("QWidget {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 5px solid  rgb(57, 210, 192);\n"
"    border-radius: 0 0 0 10px;\n"
"}\n"
"")
        self.widget_20.setObjectName("widget_20")
        self.widget.raise_()
        self.widget_4.raise_()
        self.widget_13.raise_()
        self.widget_14.raise_()
        self.widget_3.raise_()
        self.widget_15.raise_()
        self.widget_16.raise_()
        self.widget_17.raise_()
        self.widget_18.raise_()
        self.widget_19.raise_()
        self.widget_20.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1513, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setMaximumSize(QtCore.QSize(16777215, 1))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setItalic(False)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CV- Attendance Management system"))
        self.label_5.setText(_translate("MainWindow", "CV-"))
        self.label_6.setText(_translate("MainWindow", " AMS"))
        self.label_4.setText(_translate("MainWindow", "Attendance Management system"))
        self.label_3.setText(_translate("MainWindow", "CV-AMS"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "User Name"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter your user name"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.pushButton.setText(_translate("MainWindow", "Log In"))
        self.label_7.setText(_translate("MainWindow", " © 2023-2024 The Project Team. All rights reserved."))
        self.label_8.setText(_translate("MainWindow", "Designed by The Project Team. v1.0.0"))
