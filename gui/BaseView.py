from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView
from PyQt5.uic import loadUi
from PyQt5 import QtSql
import sqlite3

class BaseView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/BaseView.ui', self)
        self.pushButtonChoose.released.connect(self.choose_button_clicked)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        print("base")
        self.tableView.clicked.connect(self.selectChanged)


    @pyqtSlot()
    def selectChanged(self):
        row = self.tableView.selectionModel().selectedRows()[0].row()
        record = self.model.record(row) #.value(column);
        self.current_record = dict()
        for i in range(record.count()):
            self.current_record[record.fieldName(i)] = record.value(i)
        print(self.current_record)
        self.name=self.current_record.get("Name")
        self.PPM=self.current_record.get("PPM")
        self.PYD=self.current_record.get("PYD")
        self.PLM=self.current_record.get("PLM")
        self.M_M=self.current_record.get("M_M")
        self.B=self.current_record.get("B")
        self.YEMP=self.current_record.get("YEMP")
        self.KDM=self.current_record.get("KDM")
        self.MDM=self.current_record.get("MDM")
        self.E_z=self.current_record.get("E_z")
        self.E_up=self.current_record.get("E_up")
        print (self.name, self.PPM,self.PYD, self.PLM, self.M_M, self.B, self.YEMP, self.KDM, self.MDM, self.E_z, self.E_up)

    @pyqtSlot()
    def choose_button_clicked(self):
        """
        Выбран материал
        :return:
        """
        print("Choosed record")
        if self.tableView.selectionModel().hasSelection():
            self.selectChanged()
            self.close()
        else:
            print("Нет выбранных строк")



    def show_db_view(self, name,sql):
        print("Вывод бд:", name)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(name)
        db.open()
        model = QtSql.QSqlQueryModel()
        model.setQuery(sql)
        self.model = model
        self.tableView.setModel(model)
        cell_text = self.tableView.selectionModel().selectedRows()
        print(cell_text)
        db.close()
        self.show()