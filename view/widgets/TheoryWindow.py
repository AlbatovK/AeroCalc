from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from domain.AssetManager import get_layout_path
from view.viewmodel.TheoryViewModel import TheoryViewModel
from view.widgets import EnteringWindow


class TheoryWindow(QMainWindow):
    up_force_signal = pyqtSignal(float)
    resistance_signal = pyqtSignal(float)
    reinolds_signal = pyqtSignal(float)

    def __init__(self):
        super().__init__()
        self.view_model = TheoryViewModel(self.up_force_signal, self.resistance_signal, self.reinolds_signal)
        self.init_ui()

    def init_ui(self):
        uic.loadUi(get_layout_path("theory.ui"), self)

        def open_main():
            self.window = EnteringWindow.EnteringWindow()
            self.window.show()
            self.close()

        self.back_btn.clicked.connect(open_main)

        def take_info():
            p, v, s = self.p_edit.toPlainText(), self.v_edit.toPlainText(), self.s_edit.toPlainText()
            c_y, c_x = self.c_y_edit.toPlainText(), self.c_x_edit.toPlainText()
            th, hord, m = self.th_edit.toPlainText(), self.hord_edit.toPlainText(), self.m_edit.toPlainText()
            return p, v, s, c_y, c_x, th, hord, m

        def count_up_force():
            try:
                info = list(map(float, take_info()))
                self.view_model.count_up_force(info[0], info[1], info[3], info[2])
            except Exception as e:
                self.res_label.setText("Данные не введены или введены неверно")
                print(e)

        def count_resistance():
            try:
                info = list(map(float, take_info()))
                self.view_model.count_resistance(info[0], info[1], info[4], info[2])
            except Exception as e:
                self.res_label.setText("Данные не введены или введены неверно")
                print(e)

        def count_reinolds():
            try:
                info = list(map(float, take_info()))
                self.view_model.count_reinolds(info[0], info[5], info[6], info[7])
            except Exception as e:
                self.res_label.setText("Данные не введены или введены неверно")
                print(e)

        self.find_1.clicked.connect(count_up_force)
        self.find_2.clicked.connect(count_resistance)
        self.find_3.clicked.connect(count_reinolds)

        def display_value(val):
            self.res_label.setText(str(val))
            print(val)

        self.up_force_signal.connect(display_value)
        self.resistance_signal.connect(display_value)
        self.reinolds_signal.connect(display_value)
