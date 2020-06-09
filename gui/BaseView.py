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
        print("base")
        # selectionModel = self.tableView.selectionModel()
        # print(self.tableView.selectionModel())
        self.tableView.clicked.connect(self.selectChanged)
        # self.
        # print(db_name)
        # self.show()

    @pyqtSlot()
    def selectChanged(self):
        indexes = self.tableView.selectionModel().selectedRows()
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())
        # print(selected)

    @pyqtSlot()
    def choose_button_clicked(self):
        """
        Выбран материал
        :return:
        """
        print("Choosed record")
        print(self.tableView.selectionModel().selectedRows())

        self.close()

    def show_db_view(self, name,sql):
        print("Вывод бд:", name)
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(name)
        db.open()
        model = QtSql.QSqlQueryModel()
        model.setQuery(sql)
        self.tableView.setModel(model)
        cell_text = self.tableView.selectionModel().selectedRows()
        print(self.tableView.selectionModel().selectedRows(), self.tableView.selectionModel().selectedColumns())
        print(cell_text)
        db.close()
        self.show()