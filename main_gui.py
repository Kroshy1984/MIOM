import sys
from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import QApplication

from gui.MainWindow import MainWindow
from core.FirstPhase import Inductor
from core.SecondPhase import Pascal
from controller.MiomController import MiomContrioller
if __name__ == '__main__':

    app = QApplication(sys.argv)

    #TODO: проверить работоспособность переводчика
    translator = QTranslator(app)
    locale = QLocale.system().name()
    print(locale)
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    print(path)
    translator.load('qt_%s' % locale, path)
    app.installTranslator(translator)

    model_firs_phase = Inductor()
    model_second_phase = Pascal()
    controller = MiomContrioller(model_firs_phase, model_second_phase)
    model_firs_phase.addObserver(controller)
    model_second_phase.addObserver(controller)
    # window = MainWindow()
    # window.show()

    sys.exit(app.exec_())