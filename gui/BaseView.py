from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtSql
from PyQt5 import QtCore
from PyQt5 import QtGui
import sqlite3

class BaseView(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # QDialog.__init__(self, parent)
        loadUi('./gui/BaseView.ui', self)
        self.pushButtonChoose.released.connect(self.choose_button_clicked)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        print("base")
        self.tableView.clicked.connect(self.selectChanged_billet)
        # self.setWindowModality(QtCore.Qt.WindowModal)
        # self.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        # self.parent


    @pyqtSlot()
    def selectChanged_billet(self):
        print("billet")
        row = self.tableView.selectionModel().selectedRows()[0].row()
        record = self.model.record(row) #.value(column);
        current_record = dict()
        for i in range(record.count()):
            current_record[record.fieldName(i)] = record.value(i)
        print(current_record)
        self.current_record_billet = current_record
        self.name=current_record.get("Name")
        self.PPM=current_record.get("PPM")
        self.PYD=current_record.get("PYD")
        self.PLM=current_record.get("PLM")
        self.M_M=current_record.get("M_M")
        self.B=current_record.get("B")
        self.YEMP=current_record.get("YEMP")
        self.KDM=current_record.get("KDM")
        self.MDM=current_record.get("MDM")
        self.E_z=current_record.get("E_z")
        self.E_up=current_record.get("E_up")
        self.W_mash=current_record.get("W_mash")
        self.CCE=current_record.get("CCE")
        self.LCE=current_record.get("LCE")
        self.FCE=current_record.get("FCE")
        self.Ro=current_record.get("Ro")
        self.FW=current_record.get("FW")
        print(self.name, self.PPM, self.PYD, self.PLM, self.M_M, self.B, self.YEMP, self.KDM, self.MDM, self.E_z,
              self.E_up)
        print(self.W_mash, self.CCE, self.LCE, self.FCE, self.Ro, self.FW)

    @pyqtSlot()
    def selectChanged_inductor(self):
        print("inductor")
        row = self.tableView.selectionModel().selectedRows()[0].row()
        record = self.model.record(row)  # .value(column);
        current_record = dict()
        for i in range(record.count()):
            current_record[record.fieldName(i)] = record.value(i)
        print(current_record)
        self.current_record_inductor = current_record


    @pyqtSlot()
    def selectChanged_machines(self):
        print("machines")
        row = self.tableView.selectionModel().selectedRows()[0].row()
        record = self.model.record(row)  # .value(column);
        current_record = dict()
        for i in range(record.count()):
            current_record[record.fieldName(i)] = record.value(i)
        print(current_record)
        self.current_record_machine = current_record



    @pyqtSlot()
    def choose_button_clicked(self):
        """
        Выбран материал
        :return:
        """
        print("Choosed record")
        if self.tableView.selectionModel().hasSelection():
            # self
            # self.selectChanged_billet()
            if self.current_slot == "billet":
                self.selectChanged_billet()
            elif self.current_slot == "inductor":
                self.selectChanged_inductor()
            elif self.current_slot == "machines":
                self.selectChanged_machines()
            else:
                print("Нет подходящего слота")
            self.close()
        else:
            print("Нет выбранных строк")



    def show_db_view(self, name, sql, name_slot):
        print("Вывод бд:", name)
        self.current_slot = name_slot
        self.tableView.clicked.disconnect()
        if name_slot == "billet":
            self.tableView.clicked.connect(self.selectChanged_billet)
        elif name_slot == "inductor":
            self.tableView.clicked.connect(self.selectChanged_inductor)
        elif name_slot == "machines":
            self.tableView.clicked.connect(self.selectChanged_machines)
        else:
            print("Нет подходящего слота")
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
