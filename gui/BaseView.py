from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QDialog, QInputDialog, QErrorMessage, QMessageBox, \
    QAbstractButton
from PyQt5.uic import loadUi
from PyQt5 import QtSql
from gui.AddRecord import AddRecord
from gui.AddMachine import AddMachine
from utils.tex_to_qpixmap import mathTex_to_QPixmap
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
        self.pushButtonDelete.released.connect(self.delete_button_clicked)
        self.pushButtonEdit.released.connect(self.edit_button_clicked)
        self.pushButtonClose.released.connect(self.close_button_clicked)
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
                self.close()
                # проверка E_z


            elif self.current_slot == "inductor":
                self.selectChanged_inductor()
                self._caller_view.set_inductor_material(self.current_record_inductor)
                self.close()
            elif self.current_slot == "machines":
                self.selectChanged_machines()
                self._caller_view.machine = self.current_record_machine
                self._caller_view.set_machine(self.current_record_machine)
                self.close()
            else:
                print("Нет подходящего слота")

        else:
            print("Нет выбранных строк")

    def show_db_view(self, name, sql, name_slot):
        print("Вывод бд:", name)
        self.current_db_name = name
        self.current_slot = name_slot
        self.tableView.clicked.disconnect()
        if name_slot == "billet":
            self.tableView.clicked.connect(self.selectChanged_billet)
            self.setWindowTitle("База материалов")
            self.current_table_name = "material"
        elif name_slot == "inductor":
            self.tableView.clicked.connect(self.selectChanged_inductor)
            self.setWindowTitle("База материалов")
            self.current_table_name = "material"
        elif name_slot == "machines":
            self.tableView.clicked.connect(self.selectChanged_machines)
            self.setWindowTitle("База установок")
            self.current_table_name = "Mashines"
        else:
            print("Нет подходящего слота")
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(name)
        db.open()
        model = QtSql.QSqlQueryModel()
        # model = QtSql.QSqlTableModel()
        # model.setTable('material')
        # model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        # model.select()
        model.setQuery(sql)
        self.model = model
        print(type(self.model))
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()
        cell_text = self.tableView.selectionModel().selectedRows()
        print(cell_text)
        db.close()
        self.change_headers()
        self.tableView.resizeColumnsToContents()
        self.show()

    @pyqtSlot()
    def add_button_clicked(self):
        """
        Вызов окна для  добавления записи
        :return:
        """
        print("add_button_clicked")
        self.show_add_record_view()


    def add_record(self, record, update):
        # открытие БД
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.current_db_name)
        db.open()
        query = QtSql.QSqlQuery(db)
        # Добавление новой записи
        print(record.keys())
        sql = "select * from {0}".format(self.current_table_name)
        print(sql)
        print(','.join(record.keys()))
        print(','.join(''+str(i)+'' for i in record.values()))
        if update:

            up_str = ''
            for key in record:
                if key != 'Name':
                    if record[key] == '':
                        up_str += key + '=NULL,'
                    else:
                        up_str += key + '=' + record[key]+','
            print(up_str)
            print(up_str[-1])
            up_str = up_str[:-1]
            print(up_str)
            sql = "update {0} set {1} where Name='{2}';".format(self.current_table_name, up_str, record['Name'])
        else:
            sql = "insert into {0} ({1}) values({2});".format(self.current_table_name, ','.join(record.keys()), ','.join(record.values()))

        print(sql)
        query.exec_(sql)

        # обновление вида
        sql = "select * from {0}".format(self.current_table_name)
        print(sql)
        self.model.setQuery(sql)
        db.close()

        # if self.current_slot in ["billet", "inductor"]:
        #     self.rec = AddRecord()
        # elif self.current_slot in ["machines"]:
        #     self.rec = AddMachine()

    def show_add_record_view(self):
        if self.current_slot in ["billet", "inductor"]:
            self.rec = AddRecord(bd_view=self)
        elif self.current_slot in ["machines"]:
            self.rec = AddMachine(bd_view=self)
        self.rec.show()

    @pyqtSlot()
    def edit_button_clicked(self):
        """
        Удаление записи из базы данных
        :return:
        """
        print("edit_record")


        if self.tableView.selectionModel().hasSelection():
            row = self.tableView.selectionModel().selectedRows()[0].row()
            record = self.model.record(row)  # .value(column);
            current_record = dict()
            for i in range(record.count()):
                current_record[record.fieldName(i)] = record.value(i)
            print(current_record)

            if self.current_slot in ["billet", "inductor"]:
                self.rec = AddRecord(bd_view=self, record=current_record)
            elif self.current_slot in ["machines"]:
                self.rec = AddMachine(bd_view=self, record=current_record)
            self.rec.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Не выбрана строка!")
            msg.setWindowTitle("Предупреждение")
            msg.exec_()
            print("Нет выбранных строк")


    @pyqtSlot()
    def delete_button_clicked(self):
        """
        Удаление записи из базы данных
        :return:
        """
        print("delete_record")
        if self.tableView.selectionModel().hasSelection():
            row = self.tableView.selectionModel().selectedRows()[0].row()
            record = self.model.record(row)  # .value(column);
            current_record = dict()
            for i in range(record.count()):
                current_record[record.fieldName(i)] = record.value(i)
            print(current_record)
            print(row)
            # открытие БД
            db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(self.current_db_name)
            db.open()
            # print()
            # self.model.removeRow(self.tableView.currentIndex().row())
            query = QtSql.QSqlQuery(db)
            # удаление по имени материала
            sql = "delete from {0} where Name='{1}'".format(self.current_table_name, current_record['Name'])
            print(sql)


            # msg = QMessageBox()
            # btn = QAbstractButton()
            # btn.setText("Да")
            # msg.addButton(btn, QMessageBox.YesRole)
            # # msg.addButton(QAbstractButton("Нет"), QMessageBox.YesRole)
            # btnNo = QAbstractButton()
            # btnNo.setText("Нет")
            # msg.addButton(btnNo, QMessageBox.NoRole)

            # msg.exec_()
            # if msg.clickedButton() == btn:
            #     print('Yes clicked.')
            #     print("Удаление строки ")
            #     query.exec_(sql)
            # else:
            #     print('No clicked.')
            buttonReply = QMessageBox.question(self, 'Подтвердить удаление', "Удалить {0}?".format(current_record['Name']),
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if buttonReply == QMessageBox.Yes:
                print('Yes clicked.')
                print("Удаление строки ")
                query.exec_(sql)
            else:
                print('No clicked.')

            # обновление вида
            sql = "select* from {0}".format(self.current_table_name)
            print(sql)
            self.model.setQuery(sql)
            db.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Не выбрана строка!")
            msg.setWindowTitle("Предупреждение")
            msg.exec_()
            print("Нет выбранных строк")

    @pyqtSlot()
    def close_button_clicked(self):
        """
        Закрытие окна
        :return:
        """
        self.close()



    def change_headers(self):
        qpixmaps = []
        indx = 0
        headerLabels = [
            'Марка',
            '$(PPM), \\sigma_{u} \cdot 10^7, Pa$',
            '$(PYM), \\sigma_{y} \cdot 10^7, Pa$',
            '$(PLM), \\rho_{u} \cdot 10^3, kg/m^3$',
            '$(MM), m_{m}$',
            '$(BCM), B \cdot 10^7, Pa$',
            '$(YEM), \\rho_{e} \cdot 10^{-8}, \Omega_{m}$',
            '$(KDM), K_{d} $',
            '$E_z$',
            '$E_up$'
            # '$C_{soil}=(1 - n) C_m + \\theta_w C_w$',
            # '$k_{soil}=\\frac{\\sum f_j k_j \\theta_j}{\\sum f_j \\theta_j}$',
            # '$\\lambda_{soil}=k_{soil} / C_{soil}$'
        ]
        fontsize = 12
        for labels in headerLabels:
            qpixmaps.append(mathTex_to_QPixmap(labels, fontsize))
            self.tableView.setColumnWidth(indx, qpixmaps[indx].size().width() + 16)
            indx += 1

        print(self.tableView.horizontalHeader())

        # self.tableView.horizontalHeader().qpixmaps = qpixmaps
        # self.tableView.horizontalHeader().setHorizontalHeaderLabels(headerLabels)
        # self.tableView.horizontalHeader().setStretchLastSection(True)

        # super(self.tableView).setHorizontalHeaderLabels(headerLabels)