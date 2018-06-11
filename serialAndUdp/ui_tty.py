# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tty.ui'
#
# Created: Wed Mar 25 19:13:40 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ttyBasic(object):
    def setupUi(self, ttyBasic):
        ttyBasic.setObjectName(_fromUtf8("ttyBasic"))
        ttyBasic.resize(520, 113)
        self.verticalLayout = QtGui.QVBoxLayout(ttyBasic)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(ttyBasic)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEditPort = QtGui.QLineEdit(ttyBasic)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.lineEditPort.setFont(font)
        self.lineEditPort.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))
        self.horizontalLayout_3.addWidget(self.lineEditPort)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_2 = QtGui.QLabel(ttyBasic)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditBauds = QtGui.QLineEdit(ttyBasic)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.lineEditBauds.setFont(font)
        self.lineEditBauds.setText(_fromUtf8(""))
        self.lineEditBauds.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditBauds.setObjectName(_fromUtf8("lineEditBauds"))
        self.horizontalLayout_2.addWidget(self.lineEditBauds)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(ttyBasic)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(ttyBasic)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btSend = QtGui.QPushButton(ttyBasic)
        self.btSend.setObjectName(_fromUtf8("btSend"))
        self.horizontalLayout.addWidget(self.btSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbRcvTxt = QtGui.QLabel(ttyBasic)
        self.lbRcvTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.lbRcvTxt.setObjectName(_fromUtf8("lbRcvTxt"))
        self.verticalLayout.addWidget(self.lbRcvTxt)

        self.retranslateUi(ttyBasic)
        QtCore.QMetaObject.connectSlotsByName(ttyBasic)

    def retranslateUi(self, ttyBasic):
        ttyBasic.setWindowTitle(QtGui.QApplication.translate("ttyBasic", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ttyBasic", "Port :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ttyBasic", "Bauds", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditBauds.setInputMask(QtGui.QApplication.translate("ttyBasic", "000000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ttyBasic", "Text : ", None, QtGui.QApplication.UnicodeUTF8))
        self.btSend.setText(QtGui.QApplication.translate("ttyBasic", "&Send", None, QtGui.QApplication.UnicodeUTF8))
        self.lbRcvTxt.setText(QtGui.QApplication.translate("ttyBasic", "Received text", None, QtGui.QApplication.UnicodeUTF8))

