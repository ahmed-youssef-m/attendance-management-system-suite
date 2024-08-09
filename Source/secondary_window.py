from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecondaryWindow(object):
    def setupUi(self, SecondaryWindow):
        SecondaryWindow.setObjectName("SecondaryWindow")
        SecondaryWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SecondaryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(350, 250, 100, 30))
        self.backButton.setObjectName("backButton")
        SecondaryWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(SecondaryWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondaryWindow)

    def retranslateUi(self, SecondaryWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondaryWindow.setWindowTitle(_translate("SecondaryWindow", "Secondary Window"))
        self.backButton.setText(_translate("SecondaryWindow", "Back to Main"))
