#
# Created By Jasmine Jones
# 
from cmath import sqrt
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
import openpyxl
import os
from random import uniform
from reportlab.lib.pagesizes import letter
import textwrap
from reportlab.lib import colors
from datetime import datetime

class Ui_MainWindow(object):

    def check(self,xo):
        #Column#
        if self.pushButton_3.text() == xo and self.pushButton_2.text() == xo and self.pushButton.text() == xo:
            return True
        elif self.pushButton_8.text() == xo and self.pushButton_6.text() == xo and self.pushButton_4.text() == xo:
            return True   
        elif self.pushButton_9.text() == xo and self.pushButton_7.text() == xo and self.pushButton_5.text() == xo:
            return True 
        #Row#
        elif self.pushButton.text() == xo and self.pushButton_6.text() == xo and self.pushButton_7.text() == xo:
            return True
        elif self.pushButton_2.text() == xo and self.pushButton_4.text() == xo and self.pushButton_5.text() == xo:
            return True
        elif self.pushButton_3.text() == xo and self.pushButton_8.text() == xo and self.pushButton_9.text() == xo:
            return True
        #Diagonal#
        elif self.pushButton_9.text() == xo and self.pushButton_4.text() == xo and self.pushButton.text() == xo:
            return True
        elif self.pushButton_7.text() == xo and self.pushButton_4.text() == xo and self.pushButton_3.text() == xo:
            return True


    def opponent(self, count):
        xo = "O"
        if count == 9:
            self.label.setText("Tie!")
        elif self.check(xo) == True:
            self.label.setText("")
        elif self.check(xo) == False:
            #find random enabled button to push#
            z = int(uniform(1,10))

    def x_btn(self,btn):
        xo = "X"
        match btn:
            case 1:
                self.pushButton.setText("X")
                self.pushButton.setDisabled(True)
                
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#
            case 2:
                self.pushButton_2.setText("X")
                self.pushButton_2.setDisabled(True)
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#
            case 3:
                self.pushButton_3.setText("X")
                self.pushButton_3.setDisabled(True)
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#
            case 4:
                self.pushButton_4.setText("X")
                self.pushButton_4.setDisabled(True)
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#
            case 5:
                self.pushButton_5.setText("X")
                self.pushButton_5.setDisabled(True)
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#
            case 6:
                self.pushButton_6.setText("X")
                self.pushButton_6.setDisabled(True)
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#
            case 7:
                self.pushButton_7.setText("X")
                self.pushButton_7.setDisabled(True)
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#
            case 8:
                self.pushButton_8.setText("X")
                self.pushButton_8.setDisabled(True)
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#
            case 9:
                self.pushButton_9.setText("X")
                self.pushButton_9.setDisabled(True)
                if self.check(xo) == False:
                    self.label.setText("Computer's Turn...")
                    time.sleep(1)
                    self.count = self.count + 1
                    self.opponent(self.count)
                else:
                    self.label.setText("X's Won!")
                    #disable all buttons except retry#


    def retry_btn(self):
        self.pushButton.setText("")
        self.pushButton.setDisabled(False)

        self.pushButton_2.setText("")
        self.pushButton_2.setDisabled(False)

        self.pushButton_3.setText("")
        self.pushButton_3.setDisabled(False)

        self.pushButton_4.setText("")
        self.pushButton_4.setDisabled(False)

        self.pushButton_5.setText("")
        self.pushButton_5.setDisabled(False)

        self.pushButton_6.setText("")
        self.pushButton_6.setDisabled(False)

        self.pushButton_7.setText("")
        self.pushButton_7.setDisabled(False)

        self.pushButton_8.setText("")
        self.pushButton_8.setDisabled(False)

        self.pushButton_9.setText("")
        self.pushButton_9.setDisabled(False)

        count = 0

    def setupUi(self, MainWindow):
        self.count = 0

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton.clicked.connect(lambda: self.x_btn(1))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.pushButton_2.clicked.connect(lambda: self.x_btn(2))

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.pushButton_3.clicked.connect(lambda: self.x_btn(3))
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)
        self.pushButton_4.clicked.connect(lambda: self.x_btn(4))

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 2, 1, 1)
        self.pushButton_5.clicked.connect(lambda: self.x_btn(5))

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 1, 1, 1)
        self.pushButton_6.clicked.connect(lambda: self.x_btn(6))

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 2, 1, 1)
        self.pushButton_7.clicked.connect(lambda: self.x_btn(7))

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.pushButton_8.clicked.connect(lambda: self.x_btn(8))

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 3, 2, 1, 1)
        self.pushButton_9.clicked.connect(lambda: self.x_btn(9))

        #Retry Button#
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 4, 1, 1, 1)
        self.pushButton_10.clicked.connect(self.retry_btn)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_10.setText(_translate("MainWindow", "Retry?"))
        #self.pushButton_9.setText(_translate("MainWindow", "X"))
        #self.pushButton.setText(_translate("MainWindow", "X"))
        #self.pushButton_3.setText(_translate("MainWindow", "X"))
        #self.pushButton_2.setText(_translate("MainWindow", "X"))
        #self.pushButton_4.setText(_translate("MainWindow", "X"))
        #self.pushButton_5.setText(_translate("MainWindow", "X"))
        #self.pushButton_7.setText(_translate("MainWindow", "X"))
        #self.pushButton_6.setText(_translate("MainWindow", "X"))
        #self.pushButton_8.setText(_translate("MainWindow", "X"))
        self.label.setText(_translate("MainWindow", "Your Turn..."))

if __name__ == "__main__": #### Creates Scene ####
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    win = QMainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec())