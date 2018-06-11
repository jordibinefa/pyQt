# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_udp02.ui'
#
# Created: Thu Feb 26 11:37:15 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_udpBasic(object):
    def setupUi(self, udpBasic):
        udpBasic.setObjectName(_fromUtf8("udpBasic"))
        udpBasic.resize(520, 113)
        self.verticalLayout = QtGui.QVBoxLayout(udpBasic)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(udpBasic)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditIP = QtGui.QLineEdit(udpBasic)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.lineEditIP.setFont(font)
        self.lineEditIP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditIP.setObjectName(_fromUtf8("lineEditIP"))
        self.horizontalLayout_2.addWidget(self.lineEditIP)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(udpBasic)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEditPort = QtGui.QLineEdit(udpBasic)
        self.lineEditPort.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditPort.setObjectName(_fromUtf8("lineEditPort"))
        self.horizontalLayout_3.addWidget(self.lineEditPort)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(udpBasic)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(udpBasic)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btSend = QtGui.QPushButton(udpBasic)
        self.btSend.setObjectName(_fromUtf8("btSend"))
        self.horizontalLayout.addWidget(self.btSend)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lbRcvTxt = QtGui.QLabel(udpBasic)
        self.lbRcvTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.lbRcvTxt.setObjectName(_fromUtf8("lbRcvTxt"))
        self.verticalLayout.addWidget(self.lbRcvTxt)

        self.retranslateUi(udpBasic)
        QtCore.QMetaObject.connectSlotsByName(udpBasic)

    def retranslateUi(self, udpBasic):
        udpBasic.setWindowTitle(QtGui.QApplication.translate("udpBasic", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("udpBasic", "IP :", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditIP.setInputMask(QtGui.QApplication.translate("udpBasic", "000.000.000.000; ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("udpBasic", "Port :", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("udpBasic", "Text : ", None, QtGui.QApplication.UnicodeUTF8))
        self.btSend.setText(QtGui.QApplication.translate("udpBasic", "&Send", None, QtGui.QApplication.UnicodeUTF8))
        self.lbRcvTxt.setText(QtGui.QApplication.translate("udpBasic", "Received text", None, QtGui.QApplication.UnicodeUTF8))

