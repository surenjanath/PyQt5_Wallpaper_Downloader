# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(755, 608)
        font = QtGui.QFont()
        font.setFamily("MS Outlook")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QFrame#Main {\n"
"    background-color: qlineargradient(spread:pad, x1:0.472045, y1:0, x2:1.156818, y2:0.744, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(2, 32, 43, 251));\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QLabel#size{\n"
"    color : yellow;\n"
"    background-color: rgba(0, 0, 0,80);\n"
"\n"
"}\n"
"\n"
"QFrame#Preview {\n"
"    background-color: white;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton#Closed{\n"
"    background-color: rgba(0, 0,0, 0);\n"
"    color:rgba(120,115,255,255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#Closed:hover{\n"
"    color:rgba(250,223,11,255);\n"
"}\n"
"QPushButton#Closed:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#fButton,#iButton,#tButton{\n"
"    background-color: rgba(0, 0,0, 0);\n"
"    color:rgba(120,215,255,255);\n"
"    \n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#fButton:hover,#iButton:hover,#tButton:hover{\n"
"    color:rgba(250,223,11,255);\n"
"}\n"
"QPushButton#fButton:pressed,#iButton:pressed,#tButton:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#btn_generatePic,#btn_downloadPic,#btn_setWallpaper{\n"
"    border-radius:10px;\n"
"    background-color: rgba(190, 155, 255,255);\n"
"    color:rgba(0,0,0,255);\n"
"    font: 8pt;\n"
"}\n"
"QPushButton#btn_generatePic:hover,#btn_downloadPic:hover,#btn_setWallpaper:hover{\n"
"    color:rgba(255,255,200,255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 100, 229, 255), stop:1 rgba(255, 155, 255, 255));\n"
"    border-radius:10px;\n"
"    }\n"
"QPushButton#btn_generatePic:pressed,#btn_downloadPic:pressed,#btn_setWallpaper:pressed{\n"
"    border-radius:10px;\n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"\n"
"QLabel#Title{\n"
"    \n"
"    color: rgba(0,9,0,200);\n"
"    font:18pt;\n"
"}\n"
"QLabel#status{\n"
"color:yellow;\n"
"}\n"
"\n"
"\n"
"QPushButton#Expand,#Minimize{\n"
"    background-color: rgba(0, 0,0, 0);\n"
"    color:rgba(120,115,255,255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#Expand:hover,#Minimize:hover{\n"
"    color:rgba(250,223,11,255);\n"
"}\n"
"QPushButton#Expand:pressed,#Minimize:pressed{\n"
"    padding-left:1px;\n"
"    padding-top:1px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Main = QtWidgets.QFrame(self.centralwidget)
        self.Main.setGeometry(QtCore.QRect(21, 15, 190, 370))
        self.Main.setStyleSheet("")
        self.Main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main.setObjectName("Main")
        self.Title = QtWidgets.QLabel(self.Main)
        self.Title.setGeometry(QtCore.QRect(9, 30, 171, 50))
        font = QtGui.QFont()
        font.setFamily("Megrim")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setLineWidth(0)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setWordWrap(True)
        self.Title.setObjectName("Title")
        self.status = QtWidgets.QLabel(self.Main)
        self.status.setGeometry(QtCore.QRect(10, 340, 170, 16))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setWordWrap(True)
        self.status.setObjectName("status")
        self.Closed = QtWidgets.QPushButton(self.Main)
        self.Closed.setGeometry(QtCore.QRect(160, 10, 20, 20))
        self.Closed.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Closed.setFont(font)
        self.Closed.setObjectName("Closed")
        self.followme = QtWidgets.QLabel(self.Main)
        self.followme.setGeometry(QtCore.QRect(10, 250, 170, 40))
        self.followme.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color:black;")
        self.followme.setAlignment(QtCore.Qt.AlignCenter)
        self.followme.setWordWrap(True)
        self.followme.setObjectName("followme")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 290, 171, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(16)
        self.fButton.setFont(font)
        self.fButton.setStyleSheet("")
        self.fButton.setObjectName("fButton")
        self.horizontalLayout.addWidget(self.fButton)
        self.tButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.tButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(16)
        self.tButton.setFont(font)
        self.tButton.setStyleSheet("")
        self.tButton.setObjectName("tButton")
        self.horizontalLayout.addWidget(self.tButton)
        self.iButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.iButton.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(16)
        self.iButton.setFont(font)
        self.iButton.setStyleSheet("")
        self.iButton.setObjectName("iButton")
        self.horizontalLayout.addWidget(self.iButton)
        self.tButton.raise_()
        self.fButton.raise_()
        self.iButton.raise_()
        self.btn_generatePic = QtWidgets.QPushButton(self.Main)
        self.btn_generatePic.setGeometry(QtCore.QRect(10, 110, 171, 30))
        self.btn_generatePic.setStyleSheet("")
        self.btn_generatePic.setObjectName("btn_generatePic")
        self.Expand = QtWidgets.QPushButton(self.Main)
        self.Expand.setGeometry(QtCore.QRect(140, 138, 40, 81))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(32)
        self.Expand.setFont(font)
        self.Expand.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Expand.setCheckable(False)
        self.Expand.setDefault(False)
        self.Expand.setFlat(False)
        self.Expand.setObjectName("Expand")
        self.Preview_ImageOut = QtWidgets.QLabel(self.Main)
        self.Preview_ImageOut.setGeometry(QtCore.QRect(20, 151, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Sabon")
        font.setPointSize(14)
        self.Preview_ImageOut.setFont(font)
        self.Preview_ImageOut.setStyleSheet("color: rgb(85, 255, 255);")
        self.Preview_ImageOut.setText("")
        self.Preview_ImageOut.setAlignment(QtCore.Qt.AlignCenter)
        self.Preview_ImageOut.setWordWrap(True)
        self.Preview_ImageOut.setObjectName("Preview_ImageOut")
        self.btn_setWallpaper = QtWidgets.QPushButton(self.Main)
        self.btn_setWallpaper.setGeometry(QtCore.QRect(10, 220, 171, 30))
        self.btn_setWallpaper.setStyleSheet("")
        self.btn_setWallpaper.setObjectName("btn_setWallpaper")
        self.Minimize = QtWidgets.QPushButton(self.Main)
        self.Minimize.setGeometry(QtCore.QRect(140, 138, 40, 81))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(32)
        self.Minimize.setFont(font)
        self.Minimize.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Minimize.setCheckable(False)
        self.Minimize.setDefault(False)
        self.Minimize.setFlat(False)
        self.Minimize.setObjectName("Minimize")
        self.Preview = QtWidgets.QFrame(self.centralwidget)
        self.Preview.setGeometry(QtCore.QRect(200, 30, 0, 330))
        self.Preview.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Preview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Preview.setObjectName("Preview")
        self.Title_2 = QtWidgets.QLabel(self.Preview)
        self.Title_2.setGeometry(QtCore.QRect(20, 10, 281, 50))
        font = QtGui.QFont()
        font.setFamily("Megrim")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Title_2.setFont(font)
        self.Title_2.setLineWidth(0)
        self.Title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_2.setWordWrap(True)
        self.Title_2.setObjectName("Title_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.Preview)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 270, 261, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Download_text = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Download_text.setObjectName("Download_text")
        self.horizontalLayout_2.addWidget(self.Download_text)
        self.No_Downloads = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.No_Downloads.setText("")
        self.No_Downloads.setObjectName("No_Downloads")
        self.horizontalLayout_2.addWidget(self.No_Downloads)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Lenght_text = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Lenght_text.setObjectName("Lenght_text")
        self.horizontalLayout_2.addWidget(self.Lenght_text)
        self.Width = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Width.setText("")
        self.Width.setObjectName("Width")
        self.horizontalLayout_2.addWidget(self.Width)
        self.times = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.times.setObjectName("times")
        self.horizontalLayout_2.addWidget(self.times)
        self.Height = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Height.setText("")
        self.Height.setObjectName("Height")
        self.horizontalLayout_2.addWidget(self.Height)
        self.btn_downloadPic = QtWidgets.QPushButton(self.Preview)
        self.btn_downloadPic.setGeometry(QtCore.QRect(30, 300, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_downloadPic.setFont(font)
        self.btn_downloadPic.setStyleSheet("")
        self.btn_downloadPic.setObjectName("btn_downloadPic")
        self.pic_View = QtWidgets.QLabel(self.Preview)
        self.pic_View.setGeometry(QtCore.QRect(30, 50, 261, 211))
        self.pic_View.setStyleSheet("")
        self.pic_View.setText("")
        self.pic_View.setObjectName("pic_View")
        self.size = QtWidgets.QLabel(self.Preview)
        self.size.setGeometry(QtCore.QRect(30, 230, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        self.size.setFont(font)
        self.size.setObjectName("size")
        self.Preview.raise_()
        self.Main.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "WALLPAPER DOWNLOADER"))
        self.Closed.setText(_translate("MainWindow", "X"))
        self.followme.setText(_translate("MainWindow", "Follow me on "))
        self.fButton.setText(_translate("MainWindow", "E"))
        self.tButton.setText(_translate("MainWindow", "D"))
        self.iButton.setText(_translate("MainWindow", "C"))
        self.btn_generatePic.setText(_translate("MainWindow", "Generate Picture"))
        self.Expand.setText(_translate("MainWindow", "❯"))
        self.btn_setWallpaper.setText(_translate("MainWindow", "Set Wallpaper"))
        self.Minimize.setText(_translate("MainWindow", "❮"))
        self.Title_2.setText(_translate("MainWindow", "WALLPAPER PREVIEW"))
        self.Download_text.setText(_translate("MainWindow", " Downloads :"))
        self.Lenght_text.setText(_translate("MainWindow", "Lenght :"))
        self.times.setText(_translate("MainWindow", "x"))
        self.btn_downloadPic.setText(_translate("MainWindow", "Set As Wallpaper"))
        self.size.setText(_translate("MainWindow", "   File Size : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
