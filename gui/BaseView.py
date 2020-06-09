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