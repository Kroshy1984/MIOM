from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtSql
from gui.AddRecord import AddRecord
from PyQt5 import QtCore
from PyQt5 import QtGui
import sqlite3


class BaseView(QWidget):
    def __init__(self, parent=None, caller_view=None):
        QWidget.__init__(self, parent)
        # QDialog.__init__(self, parent)
        loadUi('./gui/BaseView.ui', self)
        self._caller_view = caller_view
        self.pushButtonChoose.released.connect(self.choose_button_clicked)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        print("base")
        self.tableView.clicked.connect(self.selectChanged_billet)

        self.pushButtonAddRecord.released.connect(self.add_button_clicked)
        # self.setWindowModality(QtCore.Qt.WindowModal)
        # self.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        # self.parent

    @pyqtSlot()
    def selectChanged_billet(self):
        print("billet")
        row = self.tableView.selectionModel().selectedRows()[0].row()
        record = self.model.record(row)  # .value(column);
        current_record = dict()
        for i in range(record.count()):
            current_record[record.fieldName(i)] = record.value(i)
        print(current_record)
        self.current_record_billet = current_record
        """self.name = current_record.get("Name")
        self.PLM = current_record.get("PLM")  #
        self.M_M = current_record.get("M_M")  #
        self.BCM = current_record.get("B")  #
        self.KDM = current_record.get("KDM")  #
        print(self.name, self.PLM, self.BCM, self.KDM)"""

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
        """self.name_in = self.current_record_inductor.get("Name")
        self.YEMP = self.current_record_inductor.get("YEMP")
        print(self.name_in, self.YEMP)"""

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
        """self.nama_mash = self.current_record_machine.get("Name")
        self.LCE = self.current_record_machine.get("LCE")
        self.CCE = self.current_record_machine.get("CCE")
        self.FCE = self.current_record_machine.get("FCE")
        self.FW = self.current_record_machine.get("FW")
        print(self.nama_mash, self.LCE, self.FCE, self.FW)"""

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
                self._caller_view.set_billet_material(self.current_record_billet)
            elif self.current_slot == "inductor":
                self.selectChanged_inductor()
                self._caller_view.set_inductor_material(self.current_record_inductor)
            elif self.current_slot == "machines":
                self.selectChanged_machines()
                self._caller_view.machine = self.current_record_machine
                self._caller_view.set_machine(self.current_record_machine)
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

    @pyqtSlot()
    def add_button_clicked(self):
        print("add_button_clicked")
        self.show_add_record_view()

    def show_add_record_view(self):
        self.rec = AddRecord()
        self.rec.show()