from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from domain.AssetManager import get_layout_path
from view.widgets.TheoryWindow import TheoryWindow


class EnteringWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        uic.loadUi(get_layout_path("enter.ui"), self)

        def open_theory_window():
            self.window = TheoryWindow()
            self.window.show()
            self.close()

        self.theory_btn.clicked.connect(open_theory_window)
