# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimpleValveWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(846, 113)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.shatterHzEdit = QtWidgets.QLineEdit(Form)
        self.shatterHzEdit.setEnabled(False)
        self.shatterHzEdit.setObjectName("shatterHzEdit")
        self.gridLayout.addWidget(self.shatterHzEdit, 3, 7, 1, 1)
        self.repeatsRadio = QtWidgets.QRadioButton(Form)
        self.repeatsRadio.setChecked(True)
        self.repeatsRadio.setAutoExclusive(False)
        self.repeatsRadio.setObjectName("repeatsRadio")
        self.gridLayout.addWidget(self.repeatsRadio, 1, 9, 1, 1)
        self.lengthRadio = QtWidgets.QRadioButton(Form)
        self.lengthRadio.setAutoExclusive(False)
        self.lengthRadio.setObjectName("lengthRadio")
        self.gridLayout.addWidget(self.lengthRadio, 3, 9, 1, 1)
        self.cleanRadio = QtWidgets.QRadioButton(Form)
        self.cleanRadio.setChecked(True)
        self.cleanRadio.setAutoExclusive(False)
        self.cleanRadio.setObjectName("cleanRadio")
        self.gridLayout.addWidget(self.cleanRadio, 1, 6, 1, 1)
        self.shatterRadio = QtWidgets.QRadioButton(Form)
        self.shatterRadio.setAutoExclusive(False)
        self.shatterRadio.setObjectName("shatterRadio")
        self.gridLayout.addWidget(self.shatterRadio, 3, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.shatterDutyEdit = QtWidgets.QLineEdit(Form)
        self.shatterDutyEdit.setEnabled(False)
        self.shatterDutyEdit.setObjectName("shatterDutyEdit")
        self.gridLayout.addWidget(self.shatterDutyEdit, 3, 8, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 8, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 7, 1, 1)
        self.pulseWidthEdit = QtWidgets.QLineEdit(Form)
        self.pulseWidthEdit.setObjectName("pulseWidthEdit")
        self.gridLayout.addWidget(self.pulseWidthEdit, 1, 4, 1, 1)
        self.repeatsEdit = QtWidgets.QLineEdit(Form)
        self.repeatsEdit.setObjectName("repeatsEdit")
        self.gridLayout.addWidget(self.repeatsEdit, 1, 10, 1, 1)
        self.pulseDutyEdit = QtWidgets.QLineEdit(Form)
        self.pulseDutyEdit.setEnabled(False)
        self.pulseDutyEdit.setObjectName("pulseDutyEdit")
        self.gridLayout.addWidget(self.pulseDutyEdit, 3, 5, 1, 1)
        self.pulseDelayEdit = QtWidgets.QLineEdit(Form)
        self.pulseDelayEdit.setObjectName("pulseDelayEdit")
        self.gridLayout.addWidget(self.pulseDelayEdit, 1, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 11)
        self.fromValuesRadio = QtWidgets.QRadioButton(Form)
        self.fromValuesRadio.setChecked(True)
        self.fromValuesRadio.setAutoExclusive(False)
        self.fromValuesRadio.setObjectName("fromValuesRadio")
        self.gridLayout.addWidget(self.fromValuesRadio, 1, 3, 1, 1)
        self.fromDutyRadio = QtWidgets.QRadioButton(Form)
        self.fromDutyRadio.setAutoExclusive(False)
        self.fromDutyRadio.setObjectName("fromDutyRadio")
        self.gridLayout.addWidget(self.fromDutyRadio, 3, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.offsetEdit = QtWidgets.QLineEdit(Form)
        self.offsetEdit.setObjectName("offsetEdit")
        self.gridLayout.addWidget(self.offsetEdit, 1, 2, 1, 1)
        self.lengthEdit = QtWidgets.QLineEdit(Form)
        self.lengthEdit.setEnabled(False)
        self.lengthEdit.setObjectName("lengthEdit")
        self.gridLayout.addWidget(self.lengthEdit, 3, 10, 1, 1)
        self.onsetEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onsetEdit.sizePolicy().hasHeightForWidth())
        self.onsetEdit.setSizePolicy(sizePolicy)
        self.onsetEdit.setObjectName("onsetEdit")
        self.gridLayout.addWidget(self.onsetEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.frequencyEdit = QtWidgets.QLineEdit(Form)
        self.frequencyEdit.setEnabled(False)
        self.frequencyEdit.setObjectName("frequencyEdit")
        self.gridLayout.addWidget(self.frequencyEdit, 3, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 4, 1, 1)
        self.removeButton = QtWidgets.QToolButton(Form)
        self.removeButton.setObjectName("removeButton")
        self.gridLayout.addWidget(self.removeButton, 2, 0, 1, 1)

        self.retranslateUi(Form)
        self.fromValuesRadio.clicked.connect(self.fromDutyRadio.toggle)
        self.fromDutyRadio.clicked.connect(self.fromValuesRadio.toggle)
        self.cleanRadio.clicked.connect(self.shatterRadio.toggle)
        self.shatterRadio.clicked.connect(self.cleanRadio.toggle)
        self.repeatsRadio.clicked.connect(self.lengthRadio.toggle)
        self.lengthRadio.clicked.connect(self.repeatsRadio.toggle)
        self.fromValuesRadio.toggled['bool'].connect(self.pulseWidthEdit.setEnabled)
        self.fromValuesRadio.toggled['bool'].connect(self.pulseDelayEdit.setEnabled)
        self.fromDutyRadio.toggled['bool'].connect(self.frequencyEdit.setEnabled)
        self.fromDutyRadio.toggled['bool'].connect(self.pulseDutyEdit.setEnabled)
        self.shatterRadio.toggled['bool'].connect(self.shatterHzEdit.setEnabled)
        self.shatterRadio.toggled['bool'].connect(self.shatterDutyEdit.setEnabled)
        self.repeatsRadio.toggled['bool'].connect(self.repeatsEdit.setEnabled)
        self.lengthRadio.toggled['bool'].connect(self.lengthEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.shatterHzEdit.setText(_translate("Form", "500"))
        self.repeatsRadio.setText(_translate("Form", "Repeats"))
        self.lengthRadio.setText(_translate("Form", "Length (s)"))
        self.cleanRadio.setText(_translate("Form", "Clean"))
        self.shatterRadio.setText(_translate("Form", "Shatter"))
        self.label_7.setText(_translate("Form", "Duty (/1)"))
        self.label_4.setText(_translate("Form", "Pulse Width (s)"))
        self.shatterDutyEdit.setText(_translate("Form", "0.5"))
        self.label_9.setText(_translate("Form", "Duty (/1)"))
        self.label_8.setText(_translate("Form", "Frequency (Hz)"))
        self.pulseWidthEdit.setText(_translate("Form", "0.1"))
        self.repeatsEdit.setText(_translate("Form", "5"))
        self.pulseDutyEdit.setText(_translate("Form", "0.5"))
        self.pulseDelayEdit.setText(_translate("Form", "0.1"))
        self.fromValuesRadio.setText(_translate("Form", "From Values"))
        self.fromDutyRadio.setText(_translate("Form", "From Duty"))
        self.label_6.setText(_translate("Form", "Pulse Delay (s)"))
        self.label_2.setText(_translate("Form", "Offset"))
        self.offsetEdit.setText(_translate("Form", "0.1"))
        self.lengthEdit.setText(_translate("Form", "1"))
        self.onsetEdit.setText(_translate("Form", "0.1"))
        self.label.setText(_translate("Form", "Onset"))
        self.frequencyEdit.setText(_translate("Form", "5"))
        self.label_5.setText(_translate("Form", "Frequency (Hz)"))
        self.removeButton.setText(_translate("Form", "-"))

