# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wellproArduino07.ui'
#
# Created: Thu Apr 28 19:28:21 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_wellproArduino(object):
    def setupUi(self, wellproArduino):
        wellproArduino.setObjectName(_fromUtf8("wellproArduino"))
        wellproArduino.resize(467, 391)
        self.verticalLayout_3 = QtGui.QVBoxLayout(wellproArduino)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelBit3 = QtGui.QLabel(wellproArduino)
        self.labelBit3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit3.setObjectName(_fromUtf8("labelBit3"))
        self.verticalLayout_2.addWidget(self.labelBit3)
        self.labelBit2 = QtGui.QLabel(wellproArduino)
        self.labelBit2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit2.setObjectName(_fromUtf8("labelBit2"))
        self.verticalLayout_2.addWidget(self.labelBit2)
        self.labelBit1 = QtGui.QLabel(wellproArduino)
        self.labelBit1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit1.setObjectName(_fromUtf8("labelBit1"))
        self.verticalLayout_2.addWidget(self.labelBit1)
        self.labelBit0 = QtGui.QLabel(wellproArduino)
        self.labelBit0.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBit0.setObjectName(_fromUtf8("labelBit0"))
        self.verticalLayout_2.addWidget(self.labelBit0)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.label_2 = QtGui.QLabel(wellproArduino)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBoxBit3 = QtGui.QCheckBox(wellproArduino)
        self.checkBoxBit3.setObjectName(_fromUtf8("checkBoxBit3"))
        self.verticalLayout.addWidget(self.checkBoxBit3)
        self.checkBoxBit2 = QtGui.QCheckBox(wellproArduino)
        self.checkBoxBit2.setObjectName(_fromUtf8("checkBoxBit2"))
        self.verticalLayout.addWidget(self.checkBoxBit2)
        self.checkBoxBit1 = QtGui.QCheckBox(wellproArduino)
        self.checkBoxBit1.setObjectName(_fromUtf8("checkBoxBit1"))
        self.verticalLayout.addWidget(self.checkBoxBit1)
        self.checkBoxBit0 = QtGui.QCheckBox(wellproArduino)
        self.checkBoxBit0.setObjectName(_fromUtf8("checkBoxBit0"))
        self.verticalLayout.addWidget(self.checkBoxBit0)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(wellproArduino)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(wellproArduino)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtGui.QLabel(wellproArduino)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_ms = QtGui.QLineEdit(wellproArduino)
        self.lineEdit_ms.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ms.setObjectName(_fromUtf8("lineEdit_ms"))
        self.horizontalLayout_2.addWidget(self.lineEdit_ms)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btEscr = QtGui.QPushButton(wellproArduino)
        self.btEscr.setEnabled(True)
        self.btEscr.setObjectName(_fromUtf8("btEscr"))
        self.horizontalLayout_3.addWidget(self.btEscr)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btLect = QtGui.QPushButton(wellproArduino)
        self.btLect.setEnabled(True)
        self.btLect.setObjectName(_fromUtf8("btLect"))
        self.horizontalLayout_3.addWidget(self.btLect)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btTmp = QtGui.QPushButton(wellproArduino)
        self.btTmp.setObjectName(_fromUtf8("btTmp"))
        self.horizontalLayout_3.addWidget(self.btTmp)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.setStretch(0, 10)

        self.retranslateUi(wellproArduino)
        QtCore.QMetaObject.connectSlotsByName(wellproArduino)

    def retranslateUi(self, wellproArduino):
        wellproArduino.setWindowTitle(_translate("wellproArduino", "WELLPRO - ARDUINO", None))
        self.labelBit3.setText(_translate("wellproArduino", "Bit 3", None))
        self.labelBit2.setText(_translate("wellproArduino", "Bit 2", None))
        self.labelBit1.setText(_translate("wellproArduino", "Bit 1", None))
        self.labelBit0.setText(_translate("wellproArduino", "Bit0", None))
        self.label_2.setText(_translate("wellproArduino", "TextLabel", None))
        self.checkBoxBit3.setText(_translate("wellproArduino", "Led 10 / Bit 3", None))
        self.checkBoxBit2.setText(_translate("wellproArduino", "Led 11 / Bit 4", None))
        self.checkBoxBit1.setText(_translate("wellproArduino", "Led 12 / Bit 2", None))
        self.checkBoxBit0.setText(_translate("wellproArduino", "Led 13 / Bit 0", None))
        self.label.setText(_translate("wellproArduino", "Adr: ", None))
        self.lineEdit.setText(_translate("wellproArduino", "02", None))
        self.label_3.setText(_translate("wellproArduino", "ms: ", None))
        self.lineEdit_ms.setText(_translate("wellproArduino", "500", None))
        self.btEscr.setText(_translate("wellproArduino", "Escriptura", None))
        self.btLect.setText(_translate("wellproArduino", "Lectura", None))
        self.btTmp.setText(_translate("wellproArduino", "Tmp ON", None))

