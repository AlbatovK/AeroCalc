import sys

from PyQt5.QtWidgets import QApplication

from view.widgets.EnteringWindow import EnteringWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    enter_window = EnteringWindow()
    enter_window.show()

    ex_code = app.exec()
    sys.exit(ex_code)
