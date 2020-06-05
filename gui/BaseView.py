
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi

class BaseView(QWidget):
    def __init__(self, db_name, parent=None):
        QWidget.__init__(self, parent)
        loadUi('./gui/MaterialBase.ui', self)
        print("base")
        print(db_name)
        self.show()
