from gui.MainWindow import MainWindow


class MiomContrioller():
    def __init__(self, model, model_2):
        """
        Принимает ссылку на модель.
        Создает и отображает внешний вид (gui) приложения
        :param model: ссылка на модель
        """
        self.mModel = model
        self.mModel_2 = model_2
        self.mView = MainWindow(self.mModel, self.mModel_2, self)
        self.mView.show()

    def start_inductor_calculation(self):
        """
        Расчет индуктора
        :return:
        """
        print("Controller, start_inductor_calculation")
        inductor_parameters = self.mView.get_inductor_parameters()
        inductor_parameters["type"] = "inductor"
        try:
            self.mModel.set_data_from_dict(inductor_parameters)
            # print(self.mModel)
            print("---------")
            self.mModel.calculate_inductor_parameters()
            print(self.mModel)
            # self.lineEditNumberCoilsInductor.setText(str(round(g.NCTC)))
            self.mView.initial_parameters.lineEditNumberCoilsInductor.setText(str(round(self.mModel.NCTC)))
            self.mView.initial_parameters.lineEditDiameter.setText(str(round(self.mModel.DCA * 10**3, 4)))
            self.mView.initial_parameters.lineEditInductorLength.setText(str(round(self.mModel.LCA * 10**3, 4)))
            self.mView.initial_parameters.lineEditWidthCoilInductor.setText(str(round(self.mModel.SSC* 10**3, 4)))
            self.mView.initial_parameters.lineEditHeightCoilInductor.setText(str(round(self.mModel.HSC* 10**3, 4)))

            self.mView.initial_parameters.groupBox_7.setEnabled(True)
            # raise Exception
        except Exception as exception:
            print(exception)
            text = "Неправильно введены параметры индуктора!"
            self.mView.show_message(text)

    def start_first_phase(self):
        """
        Расчет первого этапа
        :return:
        """
        print("Controller, start_first_phase")
        first_phase_parameters = self.mView.get_inductor_parameters()
        first_phase_parameters["type"] = "first_phase"
        try:
            self.mModel.set_data_from_dict(first_phase_parameters)
            # print(self.mModel)
            print("---------")
            self.mModel.calculate_inductor_parameters()
            print(self.mModel)
            self.mView.res_buttons.set_active_first_phase_button(True)
            params = {"WR": round(self.mModel.WR, 4),
                      "I00": self.mModel.I00,
                      "FP": round(self.mModel.FP, 4),
                      "DZT": round(self.mModel.DZT, 4),
                      "KEC": round(self.mModel.KEC, 4),
                      "EPS": round(self.mModel.f.EPS, 4),
                      "K1": round(self.mModel.K1, 4),
                      "K2": round(self.mModel.K2, 4),
                      "K3": round(self.mModel.K3, 4),
                      "K4": round(self.mModel.K4, 4),
                      "PM": round(self.mModel.PM, 4),
                      "name": self.mModel.name,
                      "operation": self.mModel.operation,
                      "PLM": self.mModel.PLM,
                      "PYM": self.mModel.PYM,
                      "LBT": self.mModel.LBT,
                      "DOT": self.mModel.DOT,
                      "ST": self.mModel.ST,
                      "YEMC": self.mModel.YEMC,
                      "LCE": self.mModel.LCE,
                      "CCE": self.mModel.CCE,
                      "R0": self.mView.initial_parameters.R0,
                      "YEMP": self.mModel.YEMP,
                      "NCT1": self.mModel.NCT1,
                      "NCT": self.mModel.NCT,
                      "LCA": round(self.mModel.LCA, 4),
                      "DCA": round(self.mModel.DCA, 4),
                      "PPM": self.mView.initial_parameters.PPM,
                      "HSC": self.mModel.HSC,
                      "ZB": self.mModel.ZB,
                      "A_tp": self.mView.initial_parameters.A_tp,
                      "B_tp": self.mView.initial_parameters.B_tp,
                      "HB_tp": self.mView.initial_parameters.HB_tp,
                      "LB_tp": self.mView.initial_parameters.LB_tp,
                      "DIB": round(self.mModel.f.DIB, 4),
                      "E_up": self.mView.initial_parameters.E_up,
                      "E_z": self.mView.initial_parameters.E_z

                      }
            print(params)
            self.mView.secondary_parameters._show(True, params)

        except Exception as exception:
            print(exception)
            text = "Неправильно введены параметры индуктора!"
            self.mView.show_message(text)

    def start_second_phase(self):
        """
        Расчет второго этапа
        :return:
        """
        second_phase_params = self.mView.get_second_phase_params()
        # second_phase_params["type"] = "inductor"
        try:
            self.mModel_2.set_data(second_phase_params)
            # print(self.mModel)
            # print("---------")
            self.mModel_2.calc_second_phase()
            # print(self.mModel_2)
            # self.lineEditNumberCoilsInductor.setText(str(round(g.NCTC)))
            # self.mView.initial_parameters.lineEditNumberCoilsInductor.setText(str(round(self.mModel.NCTC)))
            # self.mView.initial_parameters.lineEditDiameter.setText(str(round(self.mModel.DCA, 4)))
            # self.mView.initial_parameters.lineEditInductorLength.setText(str(round(self.mModel.LCA, 4)))
            # self.mView.initial_parameters.lineEditWidthCoilInductor.setText(str(round(self.mModel.SSC, 4)))
            # self.mView.initial_parameters.lineEditHeightCoilInductor.setText(str(round(self.mModel.HSC, 4)))
            #
            # self.mView.initial_parameters.groupBox_7.setEnabled(True)
            # raise Exception
        except Exception as exception:
            print(exception)
            text = "Неправильно введены параметры второй фазы!"
            self.mView.show_message(text)



    def modelIsChanged(self, message="", type=None, data=None):
        """
        Метод который будет вызван у наблюдателя при изменении модели.
        """
        if type < 4:
            users_result = self.mView.show_message(text=message, type=type, data=data)
        else:
            if type == 4:
                users_result = self.mView.show_table_second_phase(data)
            if type == 5:
                users_result = self.mView.show_control_parameters(data)

        return users_result
