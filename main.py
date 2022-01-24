from PySide2.QtWidgets import QApplication
from window import MainWindow
import sys


class App(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.main_window = MainWindow()
        self.main_window.show()


if __name__ == "__main__":
    app = App(sys.argv)
    app.exec_()
