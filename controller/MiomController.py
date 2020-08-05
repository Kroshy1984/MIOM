from gui.MainWindow import MainWindow

class MiomContrioller():
    def __init__(self, model):
        """
        Принимает ссылку на модель.
        Создает и отображает внешний вид (gui) приложения
        :param model: ссылка на модель
        """
        self.mModel = model
        self.mView = MainWindow(self.mModel, self)
        self.mView.show()

    def start_inductor_calculation(self):
        """
        Расчет индуктора
        :return:
        """
        print("Controller, start_inductor_calculation")
        inductor_parameters = self.mView.get_inductor_parameters()
        try:
            self.mModel.set_data_from_dict(inductor_parameters)
            raise Exception
        except:
            text = "Неправильно введены параметры индуктора!"
            self.mView.show_message(text)


    def start_first_phase(self):
        """
        Расчет первого этапа
        :return:
        """

    def start_second_phase(self):
        """
        Расчет второго этапа
        :return:
        """
