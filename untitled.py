import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot 
from wordcloud import WordCloud

from PIL import Image
from PyQt5.QtWidgets import QApplication, QFileDialog
import threading

class cloud:
    def __init__(self,text,img):
        self.mask = Image.open(img)
        self.wordcloud = WordCloud(font_path='msyhbd.ttc', background_color="white", width=800, height=400,mask=self.mask)
        self.w=text
    def show(self):
        self.wordcloud.generate(self.w)
        pyplot.imshow(self.wordcloud, interpolation='bilinear')
        pyplot.axis("off")
        pyplot.show()

def show():
    infects= threading.Thread(target=Ui_MainWindow.show)
    infects.start()
class Ui_MainWindow:
    fileInfo = None
    line=None
    @classmethod
    def show(cls):
        cl=cloud(Ui_MainWindow.line,Ui_MainWindow.fileInfo)
        cl.show()
    def change(self):
        Ui_MainWindow.fileInfo = QFileDialog.getOpenFileName(None,"选择图片", "C:/Users/Administrator/Desktop/")
        Ui_MainWindow.line=self.lineEdit.text()
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(632, 130)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 130)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/zhushen/zhushen.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 531, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 31))
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 181, 16))
        self.label_2.setObjectName("label_2")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 80, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(show)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 100, 231, 21))
        self.label_3.setObjectName("label_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
         

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "himcloud"))
        self.label.setText(_translate("MainWindow", "请输入文字"))
        self.label_2.setText(_translate("MainWindow", "请选择图片文件，作为背景图"))
        self.pushButton.setText(_translate("MainWindow", "点我选择文件"))
        self.pushButton_2.setText(_translate("MainWindow", "生成词云图片"))
        self.label_3.setText(_translate("MainWindow", "作者：by him , bilibili:Technology_him"))
import zhushen_rc

if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_MainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
