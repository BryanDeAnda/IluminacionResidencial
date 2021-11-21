from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
from ventas import *
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1201, 801)
        Form.setMaximumSize(QtCore.QSize(1201, 801))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form{\n"
"background-color:rgb(0, 0, 58);}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 0, 58);\n"
"color: rgb(255, 255, 255)")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(100, 100))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableStock = QtWidgets.QTableWidget(self.tab)
        self.tableStock.setGeometry(QtCore.QRect(250, 170, 671, 271))
        self.tableStock.setMinimumSize(QtCore.QSize(631, 0))
        self.tableStock.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.tableStock.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(98, 80, 127);")
        self.tableStock.setLineWidth(2)
        self.tableStock.setAutoScroll(True)
        self.tableStock.setObjectName("tableStock")
        self.tableStock.setColumnCount(5)
        self.tableStock.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(4, item)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(550, 30, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 22pt \"Brush Script MT\";")
        self.label_10.setObjectName("label_10")
        self.label_19 = QtWidgets.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(370, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.LineEditBuscarStock = QtWidgets.QLineEdit(self.tab)
        self.LineEditBuscarStock.setGeometry(QtCore.QRect(520, 100, 141, 21))
        self.LineEditBuscarStock.setText("")
        self.LineEditBuscarStock.setObjectName("LineEditBuscarStock")



        
        self.buscarStock = QtWidgets.QPushButton(self.tab)
        self.buscarStock.setGeometry(QtCore.QRect(720, 100, 93, 21))
        self.buscarStock.setStyleSheet("background-color: rgb(98, 80, 127)")
        self.buscarStock.setObjectName("buscarStock")
        self.buscarStock.clicked.connect(self.buscar_por_ID)




        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(340, 460, 131, 24))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab)
        self.label_22.setGeometry(QtCore.QRect(270, 500, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(270, 530, 65, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab)
        self.label_24.setGeometry(QtCore.QRect(270, 560, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab)
        self.label_25.setGeometry(QtCore.QRect(270, 590, 88, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.AgregarStockNom = QtWidgets.QLineEdit(self.tab)
        self.AgregarStockNom.setGeometry(QtCore.QRect(410, 500, 131, 21))
        self.AgregarStockNom.setObjectName("AgregarStockNom")
        self.AgregarStockCanti = QtWidgets.QLineEdit(self.tab)
        self.AgregarStockCanti.setGeometry(QtCore.QRect(410, 530, 131, 21))
        self.AgregarStockCanti.setObjectName("AgregarStockCanti")
        self.AgregarStockPres = QtWidgets.QLineEdit(self.tab)
        self.AgregarStockPres.setGeometry(QtCore.QRect(410, 560, 131, 21))
        self.AgregarStockPres.setObjectName("AgregarStockPres")
        self.AgregarStockSucur = QtWidgets.QLineEdit(self.tab)
        self.AgregarStockSucur.setGeometry(QtCore.QRect(410, 590, 131, 21))
        self.AgregarStockSucur.setObjectName("AgregarStockSucur")




        self.AgregarProducto = QtWidgets.QPushButton(self.tab)
        self.AgregarProducto.setGeometry(QtCore.QRect(360, 660, 93, 21))
        self.AgregarProducto.setStyleSheet("background-color: rgb(98, 80, 127)")
        self.AgregarProducto.setObjectName("AgregarProducto")
        self.AgregarProducto.clicked.connect(self.agregar_producto)




        self.label_26 = QtWidgets.QLabel(self.tab)
        self.label_26.setGeometry(QtCore.QRect(700, 460, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab)
        self.label_27.setGeometry(QtCore.QRect(640, 500, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.ModiStockID = QtWidgets.QLineEdit(self.tab)
        self.ModiStockID.setGeometry(QtCore.QRect(770, 500, 131, 21))
        self.ModiStockID.setObjectName("ModiStockID")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(640, 540, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.tab)
        self.label_29.setGeometry(QtCore.QRect(640, 620, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.ModiStockCant = QtWidgets.QLineEdit(self.tab)
        self.ModiStockCant.setGeometry(QtCore.QRect(770, 540, 131, 21))
        self.ModiStockCant.setObjectName("ModiStockCant")
        self.ModiStockSucu = QtWidgets.QLineEdit(self.tab)
        self.ModiStockSucu.setGeometry(QtCore.QRect(770, 620, 131, 21))
        self.ModiStockSucu.setObjectName("ModiStockSucu")



        self.ModificarProducto = QtWidgets.QPushButton(self.tab)
        self.ModificarProducto.setGeometry(QtCore.QRect(722, 660, 101, 21))
        self.ModificarProducto.setStyleSheet("background-color: rgb(98, 80, 127)")
        self.ModificarProducto.setObjectName("ModificarProducto")
        self.ModificarProducto.clicked.connect(self.modificar_producto)



        self.AlerAgregaStock = QtWidgets.QLabel(self.tab)
        self.AlerAgregaStock.setGeometry(QtCore.QRect(270, 700, 271, 21))
        self.AlerAgregaStock.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.AlerAgregaStock.setText("")
        self.AlerAgregaStock.setObjectName("AlerAgregaStock")
        self.AlerModiStock = QtWidgets.QLabel(self.tab)
        self.AlerModiStock.setGeometry(QtCore.QRect(640, 700, 261, 21))
        self.AlerModiStock.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.AlerModiStock.setText("")
        self.AlerModiStock.setObjectName("AlerModiStock")
        self.AlertaBuscarStock = QtWidgets.QLabel(self.tab)
        self.AlertaBuscarStock.setGeometry(QtCore.QRect(490, 130, 201, 21))
        self.AlertaBuscarStock.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.AlertaBuscarStock.setText("")
        self.AlertaBuscarStock.setObjectName("AlertaBuscarStock")
        self.label_40 = QtWidgets.QLabel(self.tab)
        self.label_40.setGeometry(QtCore.QRect(640, 580, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.ModiStockPres = QtWidgets.QLineEdit(self.tab)
        self.ModiStockPres.setGeometry(QtCore.QRect(770, 580, 131, 21))
        self.ModiStockPres.setObjectName("ModiStockPres")
        self.AgregarStockSucur_2 = QtWidgets.QLineEdit(self.tab)
        self.AgregarStockSucur_2.setGeometry(QtCore.QRect(410, 620, 131, 21))
        self.AgregarStockSucur_2.setObjectName("AgregarStockSucur_2")
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(270, 620, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")




        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 450, 41, 16))
        self.pushButton_5.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.mostrar_stock)




        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 270, 191, 191))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(950, 270, 191, 191))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.AgregarStockNom.raise_()
        self.tableStock.raise_()
        self.label_10.raise_()
        self.label_19.raise_()
        self.LineEditBuscarStock.raise_()
        self.buscarStock.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.AgregarStockCanti.raise_()
        self.AgregarStockPres.raise_()
        self.AgregarStockSucur.raise_()
        self.AgregarProducto.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.ModiStockID.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.ModiStockCant.raise_()
        self.ModiStockSucu.raise_()
        self.ModificarProducto.raise_()
        self.AlerAgregaStock.raise_()
        self.AlerModiStock.raise_()
        self.AlertaBuscarStock.raise_()
        self.label_40.raise_()
        self.ModiStockPres.raise_()
        self.AgregarStockSucur_2.raise_()
        self.label_39.raise_()
        self.pushButton_5.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableVentasRealizada = QtWidgets.QTableWidget(self.tab_6)
        self.tableVentasRealizada.setGeometry(QtCore.QRect(320, 210, 531, 461))
        self.tableVentasRealizada.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(98, 80, 127); ")
        self.tableVentasRealizada.setObjectName("tableVentasRealizada")
        self.tableVentasRealizada.setColumnCount(4)
        self.tableVentasRealizada.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableVentasRealizada.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVentasRealizada.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVentasRealizada.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableVentasRealizada.setHorizontalHeaderItem(3, item)



        self.BuscarVenta = QtWidgets.QPushButton(self.tab_6)
        self.BuscarVenta.setGeometry(QtCore.QRect(670, 140, 93, 21))
        self.BuscarVenta.setStyleSheet("background-color: rgb(98, 80, 127)")
        self.BuscarVenta.setObjectName("BuscarVenta")
        self.BuscarVenta.clicked.connect(self.buscar_venta_ID)



        self.label_37 = QtWidgets.QLabel(self.tab_6)
        self.label_37.setGeometry(QtCore.QRect(430, 140, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.BuscarVendaID = QtWidgets.QLineEdit(self.tab_6)
        self.BuscarVendaID.setGeometry(QtCore.QRect(490, 140, 141, 21))
        self.BuscarVendaID.setObjectName("BuscarVendaID")
        self.label_66 = QtWidgets.QLabel(self.tab_6)
        self.label_66.setGeometry(QtCore.QRect(480, 30, 221, 36))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("font: 22pt \"Brush Script MT\";")
        self.label_66.setObjectName("label_66")
        self.AlertaBusquedaVenta = QtWidgets.QLabel(self.tab_6)
        self.AlertaBusquedaVenta.setGeometry(QtCore.QRect(480, 170, 221, 21))
        self.AlertaBusquedaVenta.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.AlertaBusquedaVenta.setText("")
        self.AlertaBusquedaVenta.setObjectName("AlertaBusquedaVenta")
        self.label = QtWidgets.QLabel(self.tab_6)
        self.label.setGeometry(QtCore.QRect(30, 150, 211, 461))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_6)
        self.label_2.setGeometry(QtCore.QRect(930, 150, 211, 461))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")



        self.MostrarVentas_2 = QtWidgets.QPushButton(self.tab_6)
        self.MostrarVentas_2.setGeometry(QtCore.QRect(530, 100, 121, 28))
        self.MostrarVentas_2.setStyleSheet("background-color: rgb(98, 80, 127)")
        self.MostrarVentas_2.setObjectName("MostrarVentas_2")
        self.MostrarVentas_2.clicked.connect(self.agregar_ventas)



        self.pushButton_4 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 680, 51, 16))
        self.pushButton_4.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.mostrar_ventas)
        
        
        
        
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(330, 420, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.BuscarSucursalID = QtWidgets.QLineEdit(self.tab_4)
        self.BuscarSucursalID.setGeometry(QtCore.QRect(510, 420, 161, 21))
        self.BuscarSucursalID.setObjectName("BuscarSucursalID")




        self.BuscarSucursal = QtWidgets.QPushButton(self.tab_4)
        self.BuscarSucursal.setGeometry(QtCore.QRect(750, 420, 93, 21))
        self.BuscarSucursal.setStyleSheet("background-color:rgb(98, 80, 127)")
        self.BuscarSucursal.setObjectName("BuscarSucursal")
        self.BuscarSucursal.clicked.connect(self.buscar_sucursal_por_ID)



        self.tableBuscarSucursal = QtWidgets.QTableWidget(self.tab_4)
        self.tableBuscarSucursal.setGeometry(QtCore.QRect(380, 500, 421, 221))
        self.tableBuscarSucursal.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(98, 80, 127); ")
        self.tableBuscarSucursal.setObjectName("tableBuscarSucursal")
        self.tableBuscarSucursal.setColumnCount(3)
        self.tableBuscarSucursal.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableBuscarSucursal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBuscarSucursal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableBuscarSucursal.setHorizontalHeaderItem(2, item)
        self.label_62 = QtWidgets.QLabel(self.tab_4)
        self.label_62.setGeometry(QtCore.QRect(520, 30, 131, 36))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("font: 22pt \"Brush Script MT\";")
        self.label_62.setObjectName("label_62")
        self.tableSucursal = QtWidgets.QTableWidget(self.tab_4)
        self.tableSucursal.setGeometry(QtCore.QRect(320, 80, 541, 241))
        self.tableSucursal.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(98, 80, 127); ")
        self.tableSucursal.setObjectName("tableSucursal")
        self.tableSucursal.setColumnCount(4)
        self.tableSucursal.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableSucursal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSucursal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSucursal.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSucursal.setHorizontalHeaderItem(3, item)
        self.label_63 = QtWidgets.QLabel(self.tab_4)
        self.label_63.setGeometry(QtCore.QRect(440, 360, 291, 36))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("font: 22pt \"Brush Script MT\";")
        self.label_63.setObjectName("label_63")
        self.label_38 = QtWidgets.QLabel(self.tab_4)
        self.label_38.setGeometry(QtCore.QRect(460, 460, 251, 21))
        self.label_38.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.label_38.setText("")
        self.label_38.setObjectName("label_38")



        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 330, 41, 16))
        self.pushButton_3.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.mostrar_sucursal)




        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(60, 270, 191, 191))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(920, 270, 191, 191))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.TableProve = QtWidgets.QTableWidget(self.tab_2)
        self.TableProve.setGeometry(QtCore.QRect(260, 80, 661, 281))
        self.TableProve.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(98, 80, 127); ")
        self.TableProve.setObjectName("TableProve")
        self.TableProve.setColumnCount(5)
        self.TableProve.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableProve.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProve.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProve.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProve.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableProve.setHorizontalHeaderItem(4, item)
        self.label_64 = QtWidgets.QLabel(self.tab_2)
        self.label_64.setGeometry(QtCore.QRect(520, 30, 141, 36))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("font: 22pt \"Brush Script MT\";")
        self.label_64.setObjectName("label_64")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(530, 400, 141, 24))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setGeometry(QtCore.QRect(430, 430, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setGeometry(QtCore.QRect(430, 550, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(430, 510, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(430, 470, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.NombreProve = QtWidgets.QLineEdit(self.tab_2)
        self.NombreProve.setGeometry(QtCore.QRect(510, 430, 261, 21))
        self.NombreProve.setObjectName("NombreProve")
        self.CorreoProve = QtWidgets.QLineEdit(self.tab_2)
        self.CorreoProve.setGeometry(QtCore.QRect(510, 550, 261, 21))
        self.CorreoProve.setObjectName("CorreoProve")
        self.TeleProve = QtWidgets.QLineEdit(self.tab_2)
        self.TeleProve.setGeometry(QtCore.QRect(510, 510, 261, 21))
        self.TeleProve.setObjectName("TeleProve")
        self.DirecProve = QtWidgets.QLineEdit(self.tab_2)
        self.DirecProve.setGeometry(QtCore.QRect(510, 470, 261, 21))
        self.DirecProve.setObjectName("DirecProve")



        self.AgregarDistribuidor = QtWidgets.QPushButton(self.tab_2)
        self.AgregarDistribuidor.setGeometry(QtCore.QRect(560, 590, 81, 21))
        self.AgregarDistribuidor.setStyleSheet("background-color: rgb(98, 80, 127)")
        self.AgregarDistribuidor.setObjectName("AgregarDistribuidor")
        self.AgregarDistribuidor.clicked.connect(self.agregar_distribuidor)



        self.AlertaProve = QtWidgets.QLabel(self.tab_2)
        self.AlertaProve.setGeometry(QtCore.QRect(480, 710, 241, 21))
        self.AlertaProve.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.AlertaProve.setText("")
        self.AlertaProve.setObjectName("AlertaProve")


        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 370, 41, 16))
        self.pushButton_2.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.mostrar_distribuidor)



        self.label_42 = QtWidgets.QLabel(self.tab_2)
        self.label_42.setGeometry(QtCore.QRect(530, 630, 141, 24))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.tab_2)
        self.label_43.setGeometry(QtCore.QRect(480, 670, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.TeleProve_2 = QtWidgets.QLineEdit(self.tab_2)
        self.TeleProve_2.setGeometry(QtCore.QRect(510, 670, 131, 21))
        self.TeleProve_2.setObjectName("TeleProve_2")
        self.label_83 = QtWidgets.QLabel(self.tab_2)
        self.label_83.setGeometry(QtCore.QRect(40, 270, 191, 191))
        self.label_83.setText("")
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.tab_2)
        self.label_84.setGeometry(QtCore.QRect(950, 270, 191, 191))
        self.label_84.setText("")
        self.label_84.setObjectName("label_84")
        
        
        
        
        self.AgregarDistribuidor_4 = QtWidgets.QPushButton(self.tab_2)
        self.AgregarDistribuidor_4.setGeometry(QtCore.QRect(650, 670, 71, 21))
        self.AgregarDistribuidor_4.setStyleSheet("background-color: rgb(98, 80, 127)")
        self.AgregarDistribuidor_4.setObjectName("AgregarDistribuidor_4")
        self.AgregarDistribuidor_4.clicked.connect(self.eliminar_distribuidor)
        
        
        
        
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_65 = QtWidgets.QLabel(self.tab_5)
        self.label_65.setGeometry(QtCore.QRect(520, 30, 131, 36))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("font: 22pt \"Brush Script MT\";")
        self.label_65.setObjectName("label_65")
        self.TableEmp = QtWidgets.QTableWidget(self.tab_5)
        self.TableEmp.setGeometry(QtCore.QRect(260, 80, 661, 321))
        self.TableEmp.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(98, 80, 127); ")
        self.TableEmp.setObjectName("TableEmp")
        self.TableEmp.setColumnCount(5)
        self.TableEmp.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableEmp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableEmp.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableEmp.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableEmp.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableEmp.setHorizontalHeaderItem(4, item)
        self.EliminarEmpID = QtWidgets.QLineEdit(self.tab_5)
        self.EliminarEmpID.setGeometry(QtCore.QRect(480, 470, 151, 21))
        self.EliminarEmpID.setObjectName("EliminarEmpID")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(440, 470, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_5)
        self.label_16.setGeometry(QtCore.QRect(560, 440, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_5)
        self.label_17.setGeometry(QtCore.QRect(560, 510, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_5)
        self.label_18.setGeometry(QtCore.QRect(470, 540, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_35 = QtWidgets.QLabel(self.tab_5)
        self.label_35.setGeometry(QtCore.QRect(470, 580, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.tab_5)
        self.label_36.setGeometry(QtCore.QRect(470, 620, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.SalarioEmp = QtWidgets.QLineEdit(self.tab_5)
        self.SalarioEmp.setGeometry(QtCore.QRect(560, 620, 151, 21))
        self.SalarioEmp.setObjectName("SalarioEmp")
        self.EdadEmp = QtWidgets.QLineEdit(self.tab_5)
        self.EdadEmp.setGeometry(QtCore.QRect(560, 580, 151, 21))
        self.EdadEmp.setObjectName("EdadEmp")
        self.NombreEmp = QtWidgets.QLineEdit(self.tab_5)
        self.NombreEmp.setGeometry(QtCore.QRect(560, 540, 151, 21))
        self.NombreEmp.setObjectName("NombreEmp")
        
        
        
        self.AgregarEmpleado = QtWidgets.QPushButton(self.tab_5)
        self.AgregarEmpleado.setGeometry(QtCore.QRect(550, 700, 81, 21))
        self.AgregarEmpleado.setStyleSheet("background-color:rgb(98, 80, 127)")
        self.AgregarEmpleado.setObjectName("AgregarEmpleado")
        self.AgregarEmpleado.clicked.connect(self.agregar_empleado)



        self.EliminarEmpleado = QtWidgets.QPushButton(self.tab_5)
        self.EliminarEmpleado.setGeometry(QtCore.QRect(650, 470, 93, 21))
        self.EliminarEmpleado.setStyleSheet("background-color: rgb(98, 80, 127)")
        self.EliminarEmpleado.setObjectName("EliminarEmpleado")
        self.EliminarEmpleado.clicked.connect(self.eliminar_empleado)



        self.AlertaAgregaEmp = QtWidgets.QLabel(self.tab_5)
        self.AlertaAgregaEmp.setGeometry(QtCore.QRect(640, 700, 221, 21))
        self.AlertaAgregaEmp.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.AlertaAgregaEmp.setText("")
        self.AlertaAgregaEmp.setObjectName("AlertaAgregaEmp")
        self.AlertaElimEmpleado = QtWidgets.QLabel(self.tab_5)
        self.AlertaElimEmpleado.setGeometry(QtCore.QRect(750, 470, 181, 21))
        self.AlertaElimEmpleado.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.AlertaElimEmpleado.setText("")
        self.AlertaElimEmpleado.setObjectName("AlertaElimEmpleado")
        self.SalarioEmp_2 = QtWidgets.QLineEdit(self.tab_5)
        self.SalarioEmp_2.setGeometry(QtCore.QRect(560, 660, 151, 21))
        self.SalarioEmp_2.setObjectName("SalarioEmp_2")



        self.pushButton = QtWidgets.QPushButton(self.tab_5)
        self.pushButton.setGeometry(QtCore.QRect(570, 410, 41, 16))
        self.pushButton.setStyleSheet("font: 7pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.mostrar_empleado)



        self.label_41 = QtWidgets.QLabel(self.tab_5)
        self.label_41.setGeometry(QtCore.QRect(470, 660, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_128 = QtWidgets.QLabel(self.tab_5)
        self.label_128.setGeometry(QtCore.QRect(950, 270, 191, 191))
        self.label_128.setText("")
        self.label_128.setObjectName("label_128")
        self.label_129 = QtWidgets.QLabel(self.tab_5)
        self.label_129.setGeometry(QtCore.QRect(40, 270, 191, 191))
        self.label_129.setText("")
        self.label_129.setObjectName("label_129")
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Iluminación Residencial"))
        self.tableStock.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        item = self.tableStock.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tableStock.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableStock.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Cantidad"))
        item = self.tableStock.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Precio"))
        item = self.tableStock.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Distribuidor"))
        self.label_10.setText(_translate("Form", "Stock"))
        self.label_19.setText(_translate("Form", "ID del producto"))
        self.buscarStock.setText(_translate("Form", "Buscar"))
        self.label_21.setText(_translate("Form", "Agregar producto"))
        self.label_22.setText(_translate("Form", "Nombre"))
        self.label_23.setText(_translate("Form", "Cantidad"))
        self.label_24.setText(_translate("Form", "Precio"))
        self.label_25.setText(_translate("Form", "ID Sucursal"))
        self.AgregarProducto.setText(_translate("Form", "Guardar"))
        self.label_26.setText(_translate("Form", "Modificar producto"))
        self.label_27.setText(_translate("Form", "ID producto"))
        self.label_28.setText(_translate("Form", "Cantidad"))
        self.label_29.setText(_translate("Form", "ID sucursal"))
        self.ModificarProducto.setText(_translate("Form", "Guardar"))
        self.AlerAgregaStock.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"/span></p></body></html>"))
        self.AlerAgregaStock.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.AlerModiStock.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"/span></p></body></html>"))
        self.AlerModiStock.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.AlertaBuscarStock.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"/span></p></body></html>"))
        self.AlertaBuscarStock.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_40.setText(_translate("Form", "Precio"))
        self.label_39.setText(_translate("Form", "ID Distribuidor"))
        self.pushButton_5.setText(_translate("Form", "Mostrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Stock"))
        item = self.tableVentasRealizada.horizontalHeaderItem(0)
        item.setText(_translate("Form", " ID Venta"))
        item = self.tableVentasRealizada.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cantidad"))
        item = self.tableVentasRealizada.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Total"))
        item = self.tableVentasRealizada.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Hora"))
        self.BuscarVenta.setText(_translate("Form", "Buscar"))
        self.label_37.setText(_translate("Form", "ID"))
        self.label_66.setText(_translate("Form", "Ventas Realizadas"))
        self.AlertaBusquedaVenta.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"/span></p></body></html>"))
        self.AlertaBusquedaVenta.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.MostrarVentas_2.setText(_translate("Form", "Agregar venta"))
        self.pushButton_4.setText(_translate("Form", "Mostrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Ventas"))
        self.label_9.setText(_translate("Form", "ID de la sucursal"))
        self.BuscarSucursal.setText(_translate("Form", "Buscar"))
        item = self.tableBuscarSucursal.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Producto"))
        item = self.tableBuscarSucursal.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID Sucursal"))
        item = self.tableBuscarSucursal.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Disponible"))
        self.label_62.setText(_translate("Form", "Sucursales"))
        item = self.tableSucursal.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID Sucursal"))
        item = self.tableSucursal.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableSucursal.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Dirección"))
        item = self.tableSucursal.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Teléfono"))
        self.label_63.setText(_translate("Form", "Productos por Sucursal"))
        self.label_38.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"/span></p></body></html>"))
        self.label_38.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "Mostrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Sucursal"))
        item = self.TableProve.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.TableProve.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.TableProve.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Correo"))
        item = self.TableProve.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Teléfono"))
        item = self.TableProve.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Dirección"))
        self.label_64.setText(_translate("Form", "Proveedores"))
        self.label_30.setText(_translate("Form", "Agregar Proveedor"))
        self.label_31.setText(_translate("Form", "Nombre"))
        self.label_32.setText(_translate("Form", "Correo"))
        self.label_33.setText(_translate("Form", "Teléfono"))
        self.label_34.setText(_translate("Form", "Dirección"))
        self.AgregarDistribuidor.setText(_translate("Form", "Guardar"))
        self.AlertaProve.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"/span></p></body></html>"))
        self.AlertaProve.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "Mostrar"))
        self.label_42.setText(_translate("Form", "Eliminar Proveedor"))
        self.label_43.setText(_translate("Form", "ID"))
        self.AgregarDistribuidor_4.setText(_translate("Form", "Guardar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Distribuidor"))
        self.label_65.setText(_translate("Form", "Empleados"))
        item = self.TableEmp.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.TableEmp.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.TableEmp.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Edad"))
        item = self.TableEmp.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Salario"))
        item = self.TableEmp.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Sucursal"))
        self.label_15.setText(_translate("Form", "ID"))
        self.label_16.setText(_translate("Form", "Eliminar"))
        self.label_17.setText(_translate("Form", "Agregar"))
        self.label_18.setText(_translate("Form", "Nombre"))
        self.label_35.setText(_translate("Form", "Edad"))
        self.label_36.setText(_translate("Form", "Salario"))
        self.AgregarEmpleado.setText(_translate("Form", "Guardar"))
        self.EliminarEmpleado.setText(_translate("Form", "Guardar"))
        self.AlertaAgregaEmp.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"/span></p></body></html>"))
        self.AlertaAgregaEmp.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.AlertaElimEmpleado.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\"/span></p></body></html>"))
        self.AlertaElimEmpleado.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Mostrar"))
        self.label_41.setText(_translate("Form", "Sucursal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Empleado"))

    def mostrar_stock(self):
          conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
          cursor = conn.cursor()
          query = '''SELECT * FROM stock order by IDproducto'''
          cursor.execute(query)
          row = cursor.fetchall()
          contador = 0
          self.tableStock.setRowCount(len(row))
          for registro in row:
              self.tableStock.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
              self.tableStock.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
              self.tableStock.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
              self.tableStock.setItem(contador, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
              self.tableStock.setItem(contador, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
              contador += 1
          conn.commit()
          conn.close()
        
        
    def mostrar_distribuidor(self):
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM distribuidor order by IDdistribuidor'''
        cursor.execute(query)
        row = cursor.fetchall()
        contador = 0
        self.TableProve.setRowCount(len(row))
        for registro in row:
            self.TableProve.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
            self.TableProve.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
            self.TableProve.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
            self.TableProve.setItem(contador, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
            self.TableProve.setItem(contador, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
            contador += 1
        conn.commit()
        conn.close()

    def mostrar_empleado(self):
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM empleado order by IDempleado'''
        cursor.execute(query)
        row = cursor.fetchall()
        contador = 0
        self.TableEmp.setRowCount(len(row))
        for registro in row:
            self.TableEmp.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
            self.TableEmp.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
            self.TableEmp.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
            self.TableEmp.setItem(contador, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
            self.TableEmp.setItem(contador, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
            contador += 1
        conn.commit()
        conn.close()

    def mostrar_sucursal(self):
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM sucursal order by IDsucursal'''
        cursor.execute(query)
        row = cursor.fetchall()
        contador = 0
        self.tableSucursal.setRowCount(len(row))
        for registro in row:
            self.tableSucursal.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
            self.tableSucursal.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
            self.tableSucursal.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
            self.tableSucursal.setItem(contador, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
            contador += 1
        conn.commit()
        conn.close()
    
    def buscar_por_ID(self):
        _translate = QtCore.QCoreApplication.translate
        conn= psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        query= "SELECT * FROM stock WHERE idproducto=%s"
        codigo=self.LineEditBuscarStock.text()
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        if registros == []:
            self.AlertaBuscarStock.setText(_translate("Dialog", "ID no encontrado"))
        else:
            self.AlertaBuscarStock.setText(_translate("Dialog", ""))
            contador = 0
            self.tableStock.setRowCount(len(registros))
            for row in registros:
                self.tableStock.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableStock.setItem(contador,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tableStock.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
                self.tableStock.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[3])))
                self.tableStock.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[4])))
            contador += 1
        conn.commit()
        conn.close()
        
    def agregar_producto(self):
        _translate = QtCore.QCoreApplication.translate
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        cursor1= conn.cursor()
        cursor2= conn.cursor()
        cursor3= conn.cursor()
        query= '''INSERT INTO stock(nombreproducto, cantidadproducto, precio, iddistribuidor) VALUES (%s, %s, %s, %s)'''
        query1= '''SELECT nombreproducto FROM stock WHERE nombreproducto=%s'''
        query2= '''SELECT idproducto FROM stock WHERE nombreproducto=%s'''
        query3= '''INSERT INTO tiene(idproducto, idsucursal, cantidad) VALUES (%s, %s, %s)'''
        
        nombre = self.AgregarStockNom.text()
        cantidad = int(self.AgregarStockCanti.text())
        preci = int(self.AgregarStockPres.text())
        id_suc = int(self.AgregarStockSucur.text())
        id_dist = int(self.AgregarStockSucur_2.text())
        
        cursor.execute(query1, (nombre,))
        nom = cursor.fetchall()
        
        
        if nom == []:
            if cantidad>0 and preci>0 and id_suc>0 and id_suc<5 and id_dist>0:
                self.AlerAgregaStock.setText(_translate("Dialog", ""))
                cursor1.execute(query, (nombre, cantidad, preci, id_dist))
                cursor2.execute(query2, (nombre,))
                idn = cursor2.fetchall()
                for i in idn:
                    for n in i:
                        cursor3.execute(query3, (n, id_suc, cantidad))

                self.AgregarStockNom.setText(_translate("Dialog", ""))
                self.AgregarStockCanti.setText(_translate("Dialog", ""))
                self.AgregarStockPres.setText(_translate("Dialog", ""))
                self.AgregarStockSucur.setText(_translate("Dialog", ""))
                self.AgregarStockSucur_2.setText(_translate("Dialog", ""))
            else:
                self.AlerAgregaStock.setText(_translate("Dialog", "Datos incorrectos"))
        else:
            self.AlerAgregaStock.setText(_translate("Dialog", "El producto ya existe"))
        
        conn.commit()
        conn.close()
        
    def modificar_producto(self):
        _translate = QtCore.QCoreApplication.translate
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        cursor1= conn.cursor()
        cursor2= conn.cursor()
        cursor3= conn.cursor()
        cursor4= conn.cursor()
        query= '''UPDATE stock SET cantidadproducto=cantidadproducto+%s WHERE idproducto=%s'''
        query1= '''UPDATE stock SET precio=%s WHERE idproducto=%s'''
        query2= '''UPDATE tiene SET cantidad=cantidad+%s WHERE idproducto=%s and idsucursal=%s'''
        query3= '''SELECT idproducto FROM stock WHERE idproducto=%s'''
        query4= '''SELECT idsucursal FROM tiene WHERE idproducto=%s and idsucursal=%s'''
        
        stockID = int(self.ModiStockID.text())
        
        
        cursor3.execute(query3, (stockID,))
        num = cursor3.fetchall()
        
        cursor4.execute(query4, (stockID,int(self.ModiStockSucu.text())))
        num1 = cursor4.fetchall()
        
        if num == []:
            self.AlerModiStock.setText(_translate("Dialog", "El producto no existe"))
        else:
            if num1 != []:
                if int(self.ModiStockCant.text())>0 and int(self.ModiStockSucu.text())>0 and int(self.ModiStockSucu.text())<5 and  int(self.ModiStockPres.text())>0:
                    canti = int(self.ModiStockCant.text())
                    idsuc = int(self.ModiStockSucu.text())
                    pres = int(self.ModiStockPres.text())
                    cursor.execute(query,(canti, stockID))
                    cursor2.execute(query2,(canti, stockID, idsuc))
                    cursor1.execute(query1,(pres, stockID))
                    self.AlerModiStock.setText(_translate("Dialog", ""))
                    self.ModiStockCant.setText(_translate("Dialog", ""))
                    self.ModiStockSucu.setText(_translate("Dialog", ""))
                    self.ModiStockPres.setText(_translate("Dialog", ""))
                    self.ModiStockID.setText(_translate("Dialog", ""))
                
                else:
                    self.AlerModiStock.setText(_translate("Dialog", "Datos incorrectos"))
            else:
                self.AlerModiStock.setText(_translate("Dialog", "sucursal sin producto"))
        
        conn.commit()
        conn.close()

    def agregar_distribuidor(self):
        _translate = QtCore.QCoreApplication.translate
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        cursor1= conn.cursor()
        query= '''INSERT INTO distribuidor(nombredistribuidor, correo, telefono, direccion) VALUES (%s, %s, %s, %s)'''
        query1= '''SELECT nombredistribuidor FROM distribuidor WHERE nombredistribuidor=%s'''
        
        nom = self.NombreProve.text()
        correo = self.CorreoProve.text()
        tel = int(self.TeleProve.text())
        dire = self.DirecProve.text()
        print(nom)
        
        cursor.execute(query1, (nom,))
        nomb = cursor.fetchall()
        
        if nomb == []:
            self.AlertaProve.setText(_translate("Dialog", ""))
            cursor1.execute(query, (nom, correo, tel, dire))

            self.NombreProve.setText(_translate("Dialog", ""))
            self.CorreoProve.setText(_translate("Dialog", ""))
            self.TeleProve.setText(_translate("Dialog", ""))
            self.DirecProve.setText(_translate("Dialog", ""))
        else:
            self.AlertaProve.setText(_translate("Dialog", "Proveedor ya existe"))
        
        conn.commit()
        conn.close()
        
    def eliminar_distribuidor(self):
        _translate = QtCore.QCoreApplication.translate
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        cursor1= conn.cursor()
        query= '''DELETE FROM distribuidor where iddistribuidor=%s'''
        query1='''SELECT iddistribuidor FROM distribuidor WHERE iddistribuidor=%s'''

        idd = self.TeleProve_2.text()
        
        cursor1.execute(query1, (idd,))
        aux1 = cursor1.fetchall()
        
        if aux1 == []:
            self.AlertaProve.setText(_translate("Dialog", "ID no encontrado"))
        else:
            idd = self.TeleProve_2.text()
            cursor.execute(query, (idd,))
            self.TeleProve_2.setText(_translate("Dialog", ""))
            self.AlertaProve.setText(_translate("Dialog", ""))

        conn.commit()
        conn.close()
        
    def agregar_empleado(self):
        _translate = QtCore.QCoreApplication.translate
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''INSERT INTO empleado(nombreempleado,edad,sueldo,sucursal) VALUES (%s, %s, %s, %s)'''
        
        nombre = self.NombreEmp.text()
        edad = int(self.EdadEmp.text())
        sal = (self.SalarioEmp.text())
        suc = int(self.SalarioEmp_2.text())

        
        cursor.execute(query, (nombre,edad,sal,suc))
        

        self.AgregarStockNom.setText(_translate("Dialog", ""))
        self.AgregarStockCanti.setText(_translate("Dialog", ""))
        self.AgregarStockPres.setText(_translate("Dialog", ""))
        self.AgregarStockSucur.setText(_translate("Dialog", ""))
        self.AgregarStockSucur_2.setText(_translate("Dialog", ""))

        
        conn.commit()
        conn.close()

    def eliminar_empleado(self):
        _translate = QtCore.QCoreApplication.translate
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        cursor1= conn.cursor()
        query= '''DELETE FROM empleado where idempleado=%s'''
        query1='''SELECT idempleado FROM empleado WHERE idempleado=%s'''

        ide1 = self.EliminarEmpID.text()
        cursor1.execute(query1, (ide1,))
        aux1 = cursor1.fetchall()
        
        if aux1 == []:
            self.AlertaElimEmpleado.setText(_translate("Dialog", "ID no encontrado"))
        else:
            ide = self.EliminarEmpID.text()
            cursor.execute(query, (ide,))
            self.EliminarEmpID.setText(_translate("Dialog", ""))
            self.AlertaElimEmpleado.setText(_translate("Dialog", ""))

        conn.commit()
        conn.close()

    def buscar_sucursal_por_ID(self):
        _translate = QtCore.QCoreApplication.translate
        conn= psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        query= "SELECT * FROM tiene WHERE idsucursal=%s"
        codigo=self.BuscarSucursalID.text()
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        if registros == []:
            self.label_38.setText(_translate("Dialog", "     ID no encontrado"))
        else:
            self.label_38.setText(_translate("Dialog", ""))
            contador = 0
            self.tableBuscarSucursal.setRowCount(len(registros))
            for row in registros:
                self.tableBuscarSucursal.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableBuscarSucursal.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[1])))
                self.tableBuscarSucursal.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))

            contador += 1
        conn.commit()
        conn.close()
    
    def agregar_ventas(self):
        conn= psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        query= '''INSERT INTO venta(hora, total, cantidad) VALUES (current_timestamp, 0, 0)'''
        cursor.execute(query,)
        conn.commit()
        conn.close()
        self.ventas=QtWidgets.QDialog()
        self.ui2=Ui_Form2()
        self.ui2.setupUi(self.ventas)
        self.ventas.show()
    
    def mostrar_ventas(self):
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM venta order by IDventa'''
        cursor.execute(query)
        row = cursor.fetchall()
        contador = 0
        self.tableVentasRealizada.setRowCount(len(row))
        for registro in row:
            self.tableVentasRealizada.setItem(contador, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
            self.tableVentasRealizada.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(registro[3])))
            self.tableVentasRealizada.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
            self.tableVentasRealizada.setItem(contador, 3, QtWidgets.QTableWidgetItem(str(registro[1])))
            contador += 1
        conn.commit()
        conn.close()

    def buscar_venta_ID(self):
        _translate = QtCore.QCoreApplication.translate
        conn= psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        query= "SELECT * FROM venta WHERE idventa=%s"
        codigo=self.BuscarVendaID.text()
        cursor.execute(query,(codigo,))
        registros= cursor.fetchall()
        if registros == []:
            self.AlertaBusquedaVenta.setText(_translate("Dialog", "      ID no encontrado"))
        else:
            self.AlertaBusquedaVenta.setText(_translate("Dialog", ""))
            contador = 0
            self.tableVentasRealizada.setRowCount(len(registros))
            for row in registros:
                self.tableVentasRealizada.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[0])))
                self.tableVentasRealizada.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[3])))
                self.tableVentasRealizada.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[2])))
                self.tableVentasRealizada.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[1])))

            contador += 1
        conn.commit()
        conn.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())