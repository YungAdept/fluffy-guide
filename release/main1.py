# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Coffee(object):
    def setupUi(self, Coffee):
        Coffee.setObjectName("Coffee")
        Coffee.resize(1157, 686)
        self.centralwidget = QtWidgets.QWidget(Coffee)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1141, 611))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 620, 1131, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.add.setObjectName("add")
        self.horizontalLayout.addWidget(self.add)
        self.edit = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.edit.setObjectName("edit")
        self.horizontalLayout.addWidget(self.edit)
        Coffee.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Coffee)
        self.statusbar.setObjectName("statusbar")
        Coffee.setStatusBar(self.statusbar)

        self.retranslateUi(Coffee)
        QtCore.QMetaObject.connectSlotsByName(Coffee)

    def retranslateUi(self, Coffee):
        _translate = QtCore.QCoreApplication.translate
        Coffee.setWindowTitle(_translate("Coffee", "Кофе"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Coffee", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Coffee", "Название сорта"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Coffee", "Степень обжарки"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Coffee", "Молотый/в зернах"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Coffee", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Coffee", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Coffee", "Объем упаковки"))
        self.add.setText(_translate("Coffee", "Добавить"))
        self.edit.setText(_translate("Coffee", "Изменить"))
