import sys
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication

from gui.MainWindow import MainWindow
from core.FirstPhase import Inductor
from controller.MiomController import MiomContrioller
if __name__ == '__main__':

    app = QApplication(sys.argv)
    model_firs_phase = Inductor()
    controller = MiomContrioller(model_firs_phase)

    # window = MainWindow()
    # window.show()

    sys.exit(app.exec_())