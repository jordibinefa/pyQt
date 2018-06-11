#!/usr/bin/python
# -*- coding: utf-8 -*-
# tty01.py - www.binefa.cat/blog


from PyQt4 import QtGui, QtCore, Qt
from ui_tty import Ui_ttyBasic
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
import socket, netifaces, sys
import serial

if len( sys.argv ) == 2 :
	szPort = sys.argv[1]
	nBauds = 9600
else :
	if len( sys.argv ) == 3 :
		szPort = sys.argv[1]
		nBauds = int(sys.argv[2])
	else :
		szPort = "/dev/ttyUSB0"
		nBauds = 9600
			
class widgetUdp(QtGui.QWidget, Ui_ttyBasic):
	def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
		QtGui.QWidget.__init__(self, parent, f)
		self.setupUi(self)
		self.setTitle()
		self.btSend.clicked.connect(self.funcBtSend)
		self.lineEditPort.setText(szPort)
		self.lineEditBauds.setText(str(nBauds))
		self.lineEdit.setFocus()
		self.initSerialPort(self.lineEditPort.text(),int(self.lineEditBauds.text()))
		self.temporitzador = QtCore.QTimer()
		self.connect(self.temporitzador, SIGNAL("timeout()"),self.funcioTemporitzada)
		self.temporitzador.start(100)

	def setTitle(self):
		szTitle = QString()
		szTitle = szPort + " : " + str(nBauds)
		self.setWindowTitle(szTitle)
		
	def funcBtSend(self):
		self.ser.write(self.lineEdit.text().toUtf8())

	def funcioTemporitzada(self):
		data = self.ser.read(1)
		n = self.ser.inWaiting()
		if n:
			data = data + self.ser.read(n)
		if len(data):
			print data
		#if data != darrerRx:
		#	processa(data)

	def initSerialPort(self,szSerialPort, nBaudSpeed) :
		szPort = "%s" % szSerialPort
		self.ser = serial.Serial(szPort,nBaudSpeed,timeout=0) 

	def __del__(self):
		self.ser.close()

"""
	def receive(self):
		while(self.s.hasPendingDatagrams()):
			datagram = QtCore.QByteArray()
			size = self.s.pendingDatagramSize()
			data,addr,port = self.s.readDatagram(size)
			sz = "data : %s" % str(data)
			print sz, ", len : %s, size : %s " % (str(len(data)),str(size))
			#szRcvTxt = "data : " + sz4to1(data)
			#self.lbRcvTxt.setText(szRcvTxt)
			self.lbRcvTxt.setText(data)
"""


if __name__ == '__main__':
	import sys

	app = QtGui.QApplication(sys.argv)
	window = widgetUdp()
	window.resize(400,100)
	window.show()

	sys.exit(app.exec_())
