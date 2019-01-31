from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 100, 131, 141))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("button_y.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("button_red.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(200, 200))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 280, 141, 41))
        self.pushButton_2.setText("MAN")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1_guy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 330, 141, 41))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("CARS")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("0_bike.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 380, 141, 41))
        icon2 = QtGui.QIcon()
        self.pushButton_4.setText("HOME")
        icon2.addPixmap(QtGui.QPixmap("0_home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(28, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(460, 10, 141, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(5, 300, 161, 161))
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap("0_guy.png"))
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 300, 131, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("0_home.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 320, 91, 91))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("0_bike.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class ImageViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel(self)
        self.label_0 = QLabel(self)
        pixmap = QPixmap('fon1.png')
        self.label.setPixmap(pixmap)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        self.label.resize(pixmap.width(), pixmap.height())
        self.label.move(0, 0)
        self.setWindowTitle('MainWindow')



class App(QMainWindow,Ui_MainWindow, ImageViewer):
    def __init__(self):
        super().__init__()
        self.l_car = 0
        self.l_home = 0
        self.l_man = 0
        self.n = 1
        self.a = 0
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)
        self.count = 0
        self.pushButton_2.clicked.connect(self.new_man)
        self.pushButton_3.clicked.connect(self.new_car)
        self.pushButton_4.clicked.connect(self.new_home)


    def click(self):
        self.count = self.count + ((self.a + 1)*(self.n))
        self.lcdNumber.display(self.count)

    def new_home(self):
        if self.count >= 150:
            self.l_home = 1
            self.n = 2
        if self.count >= 500:
            self.l_home = 2
            self.n = 3
        if self.count >= 800:
            self.l_home = 3
            self.n = 4
        if self.count >= 1000:
            self.l_home = 5
        q = str(self.l_home) + "_home.png"
        self.label_2.setPixmap(QtGui.QPixmap(q))
        if self.l_home >= 1:
            self.label_2.setGeometry(QtCore.QRect(120, 250, 180, 180))

    def new_car(self):
        if self.count >= 150:
            self.l_car = 1
            self.a = 1
        if self.count >= 500:
            self.l_car = 2
            self.a = 2
        if self.count >= 800:
            self.l_car = 3
            self.a = 3
        if self.count >= 1000:
            self.l_car = 3
        q1 = str(self.l_car) + '_bike.png'
        self.label_3.setPixmap(QtGui.QPixmap(q1))
        if self.l_car >= 2:
            self.label_3.setGeometry(QtCore.QRect(300, 320, 120, 120))

    def new_man(self):
        if self.count >= 150:
            self.l_man = 1
        if self.count >= 500:
            self.l_man = 2
        if self.count >= 800:
            self.l_man = 3
        if self.count >= 1000:
            self.l_man = 3
        q2 = str(self.l_man) + "_guy.png"
        self.label_1.setPixmap(QtGui.QPixmap(q2))
            
 
 
app = QApplication(sys.argv)
ex = App()
ex.show()
sys.exit(app.exec_())
