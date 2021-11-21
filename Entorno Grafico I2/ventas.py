from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1201, 801)
        Form.setMaximumSize(QtCore.QSize(1201, 801))
        Form.setStyleSheet("QWidget#Form{\n"
"background-color:rgb(0, 0, 58);}\n"
"")
        self.label_61 = QtWidgets.QLabel(Form)
        self.label_61.setGeometry(QtCore.QRect(560, 40, 81, 36))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_61.setFont(font)
        self.label_61.setStyleSheet("font: 22pt \"Brush Script MT\";\n"
"color: rgb(255, 255, 255);")
        self.label_61.setObjectName("label_61")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(480, 100, 88, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(480, 150, 65, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(480, 200, 85, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.AgregaVentaID = QtWidgets.QLineEdit(Form)
        self.AgregaVentaID.setGeometry(QtCore.QRect(590, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AgregaVentaID.setFont(font)
        self.AgregaVentaID.setStyleSheet("background-color:rgb(0, 0, 58); \n"
"color: rgb(255, 255, 255);")
        self.AgregaVentaID.setText("")
        self.AgregaVentaID.setObjectName("AgregaVentaID")
        self.AgregaVentaCant = QtWidgets.QLineEdit(Form)
        self.AgregaVentaCant.setGeometry(QtCore.QRect(590, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AgregaVentaCant.setFont(font)
        self.AgregaVentaCant.setStyleSheet("background-color:rgb(0, 0, 58); \n"
"color: rgb(255, 255, 255);")
        self.AgregaVentaCant.setText("")
        self.AgregaVentaCant.setObjectName("AgregaVentaCant")
        self.AgregaVentaSuc_2 = QtWidgets.QLineEdit(Form)
        self.AgregaVentaSuc_2.setGeometry(QtCore.QRect(590, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AgregaVentaSuc_2.setFont(font)
        self.AgregaVentaSuc_2.setStyleSheet("background-color:rgb(0, 0, 58); \n"
"color: rgb(255, 255, 255);")
        self.AgregaVentaSuc_2.setText("")
        self.AgregaVentaSuc_2.setObjectName("AgregaVentaSuc_2")
        self.GuardarVenta_2 = QtWidgets.QPushButton(Form)
        self.GuardarVenta_2.setGeometry(QtCore.QRect(560, 250, 81, 21))
        self.GuardarVenta_2.clicked.connect(self.guardar_venta)
        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GuardarVenta_2.setFont(font)
        self.GuardarVenta_2.setStyleSheet("background-color: rgb(98, 80, 127);\n"
"color: rgb(255, 255, 255);")
        self.GuardarVenta_2.setObjectName("GuardarVenta_2")
        self.AlerAgregaVenta_2 = QtWidgets.QLabel(Form)
        self.AlerAgregaVenta_2.setGeometry(QtCore.QRect(470, 290, 261, 21))
        self.AlerAgregaVenta_2.setStyleSheet("color: rgb(255, 8, 12);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"background-color:rgb(0, 0, 58);")
        self.AlerAgregaVenta_2.setText("")
        self.AlerAgregaVenta_2.setObjectName("AlerAgregaVenta_2")
        self.TableVentas_2 = QtWidgets.QTableWidget(Form)
        self.TableVentas_2.setGeometry(QtCore.QRect(140, 340, 921, 351))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.TableVentas_2.setFont(font)
        self.TableVentas_2.setToolTip("")
        self.TableVentas_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(98, 80, 127); \n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.TableVentas_2.setObjectName("TableVentas_2")
        self.TableVentas_2.setColumnCount(7)
        self.TableVentas_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableVentas_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableVentas_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableVentas_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableVentas_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableVentas_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableVentas_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableVentas_2.setHorizontalHeaderItem(6, item)
        self.label_82 = QtWidgets.QLabel(Form)
        self.label_82.setGeometry(QtCore.QRect(500, 730, 61, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_82.setFont(font)
        self.label_82.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_82.setObjectName("label_82")
        self.TotalVenta_3 = QtWidgets.QLabel(Form)
        self.TotalVenta_3.setGeometry(QtCore.QRect(580, 720, 121, 41))
        self.TotalVenta_3.setStyleSheet("background-color: rgb(98, 80, 127); \n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.TotalVenta_3.setText("")
        self.TotalVenta_3.setObjectName("TotalVenta_3")
        self.label_83 = QtWidgets.QLabel(Form)
        self.label_83.setGeometry(QtCore.QRect(140, 80, 191, 191))
        self.label_83.setStyleSheet("background-color:rgb(0, 0, 58);")
        self.label_83.setText("")
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(Form)
        self.label_84.setGeometry(QtCore.QRect(870, 80, 191, 191))
        self.label_84.setStyleSheet("background-color:rgb(0, 0, 58);")
        self.label_84.setText("")
        self.label_84.setObjectName("label_84")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_61.setText(_translate("Form", "Ventas"))
        self.label_13.setText(_translate("Form", "ID Producto"))
        self.label_7.setText(_translate("Form", "Cantidad"))
        self.label_12.setText(_translate("Form", "ID Sucursal"))
        self.GuardarVenta_2.setText(_translate("Form", "Guardar"))
        self.AlerAgregaVenta_2.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.AlerAgregaVenta_2.setWhatsThis(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        item = self.TableVentas_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", " ID Venta"))
        item = self.TableVentas_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID Producto"))
        item = self.TableVentas_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Producto"))
        item = self.TableVentas_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Cantidad"))
        item = self.TableVentas_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Precio"))
        item = self.TableVentas_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Total"))
        item = self.TableVentas_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Hora"))
        self.label_82.setText(_translate("Form", "Total"))
        
    def guardar_venta(self):
        _translate = QtCore.QCoreApplication.translate
        conn = psycopg2.connect(dbname="IluminacionResidencial", user="postgres", password="chimales12", host="localhost", port="5432")
        cursor= conn.cursor()
        cursor1= conn.cursor()
        cursor2 = conn.cursor()
        cursor3 = conn.cursor()
        cursor4 = conn.cursor()
        cursor5 = conn.cursor()
        cursor6 = conn.cursor()
        cursor7 = conn.cursor()
        cursor8 = conn.cursor()
        cursor9 = conn.cursor()
        cursor10 = conn.cursor()
        cursor11 = conn.cursor()
        cursor12 = conn.cursor()
        cursor13 = conn.cursor()
        cursor14 = conn.cursor()
        
        query = '''SELECT idventa FROM venta WHERE idventa=(SELECT max(idventa) FROM venta)'''
        query1 = '''INSERT INTO produce(idventa, idproducto, idsucursal, nombreproducto, cantidad, precio, total) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        query2 = '''SELECT * FROM stock WHERE idproducto=%s'''
        query3 = '''SELECT cantidadproducto FROM stock WHERE idproducto=%s'''
        query4 = '''SELECT nombreproducto FROM stock WHERE idproducto=%s'''
        query5 = '''UPDATE stock SET cantidadproducto=cantidadproducto-%s WHERE idproducto=%s'''
        query6 = '''SELECT precio FROM stock WHERE idproducto=%s'''
        query7 = '''SELECT idsucursal FROM tiene WHERE idproducto=%s and idsucursal=%s'''
        query8 = '''UPDATE tiene SET cantidad=cantidad-%s WHERE idproducto=%s and idsucursal=%s'''
        query9 = '''SELECT cantidad FROM tiene WHERE idproducto=%s and idsucursal=%s'''
        query10 = "SELECT * FROM produce WHERE idventa=%s"
        query11 = "SELECT hora FROM venta WHERE idventa=%s"
        query12 = '''UPDATE venta SET total=total+%s WHERE idventa=%s'''
        query13 = "SELECT total FROM venta WHERE idventa=%s"
        query14 = '''UPDATE venta SET cantidad=cantidad+%s WHERE idventa=%s'''
        
        stockID = int(self.AgregaVentaID.text())
        cantidad = int(self.AgregaVentaCant.text())
        sucID = int(self.AgregaVentaSuc_2.text())
        
        cursor.execute(query)
        venta= cursor.fetchall()
        for i in venta:
            for n in i:
                 idventa = n
                 
        cursor1.execute(query2,(stockID,))
        producto = cursor1.fetchall()
        
        cursor2.execute(query3,(stockID,))
        aux = cursor2.fetchall()
        for i in aux:
            for n in i:
                 cant = n
                 
        cursor3.execute(query4,(stockID,))
        aux1 = cursor3.fetchall()
        for i in aux1:
            for n in i:
                 nom = n
                 
        cursor6.execute(query6,(stockID,))
        aux2 = cursor6.fetchall()
        for i in aux2:
            for n in i:
                 pres = n
        
        cursor9.execute(query9,(stockID,sucID,))
        aux3 = cursor9.fetchall()
        for i in aux3:
            for n in i:
                 cantsuc = n
                 
        cursor11.execute(query11,(idventa,))
        aux4 = cursor11.fetchall()
        for i in aux4:
            for n in i:
                 horario = n
                 
        cursor7.execute(query7, (stockID,sucID))
        num1 = cursor7.fetchall()
        
        if producto != [] and cant >= cantidad and num1 != [] and cantsuc >= cantidad:
            tot = pres*cantidad
            cursor4.execute(query1,(idventa, stockID, sucID, nom, cantidad,pres, tot))
            cursor5.execute(query5,(cantidad, stockID))
            cursor8.execute(query8,(cantidad, stockID, sucID))
            self.AlerAgregaVenta_2.setText(_translate("Dialog", ""))
            cursor10.execute(query10,(idventa,))
            todasventas = cursor10.fetchall()
            self.TableVentas_2.setRowCount(len(todasventas))
            contador = 0
            for row in todasventas:
                self.TableVentas_2.setItem(contador,0,QtWidgets.QTableWidgetItem(str(row[1])))
                self.TableVentas_2.setItem(contador,1,QtWidgets.QTableWidgetItem(str(row[0])))
                self.TableVentas_2.setItem(contador,2,QtWidgets.QTableWidgetItem(str(row[3])))
                self.TableVentas_2.setItem(contador,3,QtWidgets.QTableWidgetItem(str(row[4])))
                self.TableVentas_2.setItem(contador,4,QtWidgets.QTableWidgetItem(str(row[5])))
                self.TableVentas_2.setItem(contador,5,QtWidgets.QTableWidgetItem(str(row[6])))
                self.TableVentas_2.setItem(contador,6,QtWidgets.QTableWidgetItem(str(horario)))
                contador += 1
            cursor12.execute(query12,(tot, idventa))
            todasventas = cursor10.fetchall()
            
            cursor14.execute(query14,(cantidad, idventa))
            
            cursor13.execute(query13,(idventa,))
            aux5 = cursor13.fetchall()
            for i in aux5:
                for n in i:
                     totalvent = n
            
            self.TotalVenta_3.setText(_translate("Dialog", str(totalvent)))
            self.AgregaVentaID.setText(_translate("Dialog", ""))
            self.AgregaVentaCant.setText(_translate("Dialog", ""))
            self.AgregaVentaSuc_2.setText(_translate("Dialog", ""))

        else:
            self.AlerAgregaVenta_2.setText(_translate("Dialog", "          Datos incorrectos"))
            
        
        conn.commit()
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

