from PySide2.QtCore import Qt
from PySide2.QtGui import QDoubleValidator
from PySide2.QtWidgets import QMainWindow, QStyledItemDelegate, QLineEdit, QTableWidgetItem
from window_ui import Ui_MainWindow
from utils import to_upper_hessenberg, Matrix, Vector


class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        validator = QDoubleValidator(editor)
        editor.setValidator(validator)
        return editor


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dimension = 1
        self.table_widgets = [
            self.input_matrix_table_widget,
            self.reflector_matrix_table_widget,
            self.hessenberg_matrix_table_widget
        ]
        self.transform_button.clicked.connect(self.transform_button_clicked)
        self.dimension_spin_box.valueChanged.connect(self.dimension_spin_box_value_changed)
        for table_widget in self.table_widgets:
            numerical_delegate = NumericDelegate(table_widget)
            table_widget.setItemDelegate(numerical_delegate)

    def transform_button_clicked(self):
        matrix = []
        for i in range(self.dimension):
            row = []
            for j in range(self.dimension):
                item = self.input_matrix_table_widget.item(i, j)
                row.append(float(item.text() if item is not None else 0))
            matrix.append(row)
        hessenberg, reflector = to_upper_hessenberg(matrix)
        for i in range(self.dimension):
            for j in range(self.dimension):
                item = self.reflector_matrix_table_widget.item(i, j)
                if item is None:
                    item = QTableWidgetItem()
                    self.reflector_matrix_table_widget.setItem(i, j, item)
                item.setText(str(reflector.cell(i, j)))

                item = self.hessenberg_matrix_table_widget.item(i, j)
                if item is None:
                    item = QTableWidgetItem()
                    self.hessenberg_matrix_table_widget.setItem(i, j, item)
                item.setText(str(hessenberg.cell(i, j)))

    def dimension_spin_box_value_changed(self, value):
        self.dimension = value
        for table_widget in self.table_widgets:
            table_widget.setColumnCount(value)
            table_widget.setRowCount(value)
