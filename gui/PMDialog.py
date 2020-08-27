from PyQt5.QtWidgets import QDialog, QButtonGroup
from PyQt5.uic import loadUi

class PMDialog(QDialog):
    def __init__(self, parent=None, data=None):
        QDialog.__init__(self, parent)
        loadUi('./gui/PMDialog.ui', self)
        self.l_1.setText( "PMA = " + str(round(data["PMA"], 2)))
        self.l_2.setText("PMB = " + str(round(data["PMB"], 2)))
        self.l_3.setText("PMC = " + str(round(data["PMC"], 2)))
        self.l_4.setText("PMD = " + str(round(data["PMD"], 2)))
        self.l_5.setText("PMF = " + str(round(data["PMF"], 2)))

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.rb_1, id=1)
        self.button_group.addButton(self.rb_2, id=2)
        self.button_group.addButton(self.rb_3, id=3)
        self.button_group.addButton(self.rb_4, id=4)
        self.button_group.addButton(self.rb_5, id=5)

        # self.button_group.setId(1)
        self.checked = self.button_group.checkedId()
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)
        # self.horizontalLayout.setVisible(False)
        self.label.setVisible(False)
        self.lineEdit.setVisible(False)

    # @pyqtSlot()
    def _on_radio_button_clicked(self, button):
        # print(button)
        # print(self.button_group.id())
        self.checked = self.button_group.checkedId()
        # self.checked =
        # self.label.setText('Current: ' + button.text())
