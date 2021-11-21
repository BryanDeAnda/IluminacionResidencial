from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtGui import QPixmap
from tabs import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1198, 799)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../karla/icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1201, 801))
        self.bgwidget.setStyleSheet("")
        self.bgwidget.setObjectName("bgwidget")
        self.image = QtWidgets.QLabel(self.bgwidget)
        self.image.setGeometry(QtCore.QRect(0, 0, 1201, 801))
        self.image.setStyleSheet("border-radius:50%;")
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.image.setPixmap(QPixmap('fondoiniciofuerte.jpg'))
        
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 110, 531, 101))
        self.label_2.setStyleSheet("font: italic 40pt \"Brush Script MT\"; color:rgb(255, 255, 255)\n"
"")
        self.label_2.setObjectName("label_2")
        self.login_2 = QtWidgets.QPushButton(self.bgwidget)
        self.login_2.setGeometry(QtCore.QRect(540, 520, 121, 41))
        self.login_2.setStyleSheet("border-radius:16px;\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(98, 80, 127);\n"
"font: 11pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255)")
        self.login_2.setObjectName("login_2")
        self.login_2.clicked.connect(self.iniciar_Sesion)
        
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 230, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_5.setObjectName("label_5")
        self.emailfield_2 = QtWidgets.QLineEdit(self.bgwidget)
        self.emailfield_2.setGeometry(QtCore.QRect(430, 250, 341, 51))
        self.emailfield_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";color:rgb(235, 235, 235);")
        self.emailfield_2.setText("")
        self.emailfield_2.setObjectName("emailfield_2")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 380, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("; color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Segoe UI Black\";")
        self.label_6.setObjectName("label_6")
        self.passwordfield = QtWidgets.QLineEdit(self.bgwidget)
        self.passwordfield.setGeometry(QtCore.QRect(430, 400, 341, 51))
        self.passwordfield.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";color:rgb(235, 235, 235);")
        self.passwordfield.setText("")
        self.passwordfield.setObjectName("passwordfield")
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(480, 470, 241, 31))
        self.label.setStyleSheet("color: rgb(255,255,255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Iluminación Residencial"))
        self.label_2.setText(_translate("Dialog", "Iluminación Residencial"))
        self.login_2.setText(_translate("Dialog", "Ingresar"))
        self.label_5.setText(_translate("Dialog", "Admin"))
        self.label_6.setText(_translate("Dialog", "Password"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Admin o Password incorrectos</span></p></body></html>"))
        self.label.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        
    #Funcion para el inicio de sesión   
    def iniciar_Sesion(self):
        _translate = QtCore.QCoreApplication.translate
        admin = ""
        contra = ""
        admin=self.emailfield_2.text()
        contra=self.passwordfield.text()
        
        if admin == "lamparas.65@ilumresidencial.com" and contra == "contraseña":
            self.label.setText(_translate("Dialog", ""))
            self.taps=QtWidgets.QDialog()
            self.ui=Ui_Form()
            self.ui.setupUi(self.taps)
            self.taps.show()
        else:
            self.label.setText(_translate("Dialog", "Admin o Password incorrectos"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

