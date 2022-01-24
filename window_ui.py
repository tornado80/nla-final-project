# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(901, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(15)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.dimension_spin_box = QSpinBox(self.layoutWidget)
        self.dimension_spin_box.setObjectName(u"dimension_spin_box")
        self.dimension_spin_box.setMinimum(1)
        self.dimension_spin_box.setMaximum(100)

        self.gridLayout.addWidget(self.dimension_spin_box, 1, 1, 1, 1)

        self.input_matrix_table_widget = QTableWidget(self.layoutWidget)
        if (self.input_matrix_table_widget.columnCount() < 1):
            self.input_matrix_table_widget.setColumnCount(1)
        if (self.input_matrix_table_widget.rowCount() < 1):
            self.input_matrix_table_widget.setRowCount(1)
        self.input_matrix_table_widget.setObjectName(u"input_matrix_table_widget")
        self.input_matrix_table_widget.setRowCount(1)
        self.input_matrix_table_widget.setColumnCount(1)
        self.input_matrix_table_widget.horizontalHeader().setVisible(True)
        self.input_matrix_table_widget.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.input_matrix_table_widget, 2, 0, 1, 2)

        self.transform_button = QPushButton(self.layoutWidget)
        self.transform_button.setObjectName(u"transform_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transform_button.sizePolicy().hasHeightForWidth())
        self.transform_button.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.transform_button, 3, 0, 1, 2)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.gridLayout.setColumnStretch(1, 1)
        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.reflector_matrix_table_widget = QTableWidget(self.layoutWidget1)
        if (self.reflector_matrix_table_widget.columnCount() < 1):
            self.reflector_matrix_table_widget.setColumnCount(1)
        if (self.reflector_matrix_table_widget.rowCount() < 1):
            self.reflector_matrix_table_widget.setRowCount(1)
        self.reflector_matrix_table_widget.setObjectName(u"reflector_matrix_table_widget")
        self.reflector_matrix_table_widget.setRowCount(1)
        self.reflector_matrix_table_widget.setColumnCount(1)
        self.reflector_matrix_table_widget.horizontalHeader().setVisible(True)
        self.reflector_matrix_table_widget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.reflector_matrix_table_widget)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.hessenberg_matrix_table_widget = QTableWidget(self.layoutWidget1)
        if (self.hessenberg_matrix_table_widget.columnCount() < 1):
            self.hessenberg_matrix_table_widget.setColumnCount(1)
        if (self.hessenberg_matrix_table_widget.rowCount() < 1):
            self.hessenberg_matrix_table_widget.setRowCount(1)
        self.hessenberg_matrix_table_widget.setObjectName(u"hessenberg_matrix_table_widget")
        self.hessenberg_matrix_table_widget.setRowCount(1)
        self.hessenberg_matrix_table_widget.setColumnCount(1)
        self.hessenberg_matrix_table_widget.horizontalHeader().setVisible(True)
        self.hessenberg_matrix_table_widget.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.hessenberg_matrix_table_widget)

        self.splitter.addWidget(self.layoutWidget1)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Upper Hessenberg Calculator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dimension", None))
        self.transform_button.setText(QCoreApplication.translate("MainWindow", u"Transform to Upper Hessenberg", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input Matrix (A):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Reflector (Q):", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Upper Hessenberg Form (B = Q^T * A * Q):", None))
    # retranslateUi

