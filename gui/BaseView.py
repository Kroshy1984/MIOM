from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtSql
import sqlite3

class BaseView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/BaseView.ui', self)
        self.pushButtonChoose.released.connect(self.choose_button_clicked)
        print("base")
        # print(db_name)
        # self.show()

    @pyqtSlot()
    def choose_button_clicked(self):
        """
        Выбран материал
        :return:
        """
        print("Choosed record")
        self.close()

    def show_db_view(self, name,sql):
        print("Вывод бд:", name)
        query = QtSql.QSqlQuery()
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(name)
        db.open()
        model = QtSql.QSqlQueryModel()
        model.setQuery(sql)
        self.tableView.setModel(model)
        self.show()