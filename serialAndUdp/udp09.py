#!/usr/bin/python
# -*- coding: utf-8 -*-
# udp08.py - www.binefa.cat/blog


from PyQt4 import QtGui, QtCore, Qt
from ui_udp02 import Ui_udpBasic
from PyQt4.QtCore import *
from PyQt4.QtNetwork import *
import socket, netifaces, sys

if len( sys.argv ) == 2 :
	nUdpPort = int(sys.argv[1])
else :
	nUdpPort = 6005
	
def szCurrentIP() :
	interfaces = netifaces.interfaces()
	for i in interfaces:
		if i == 'lo':
			continue
		iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
		if iface != None:
			for j in iface:
				return j['addr']
				
def sz4to1(data):
	sz = QString()
	for i in range(len(str(data))) :
		if not (i % 4) :
			# print data[i]
			sz += data[i]
	return sz
				
class widgetUdp(QtGui.QWidget, Ui_udpBasic):
	def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
		QtGui.QWidget.__init__(self, parent, f)
		self.setupUi(self)
		self.setTitle()
		self.btSend.clicked.connect(self.funcBtSend)
		self.listenToUdpMsg()
		self.lineEditIP.setText(szCurrentIP())
		self.lineEditPort.setText(str(nUdpPort))

	def setTitle(self):
		szTitle = QString()
		szTitle = szCurrentIP() + " : " + szTitle.setNum(nUdpPort)
		self.setWindowTitle(szTitle)
		
	def funcBtSend(self):
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		client_socket.sendto(self.lineEdit.text().toUtf8(), (self.lineEditIP.text(),int(self.lineEditPort.text())))
		client_socket.close()

	def listenToUdpMsg(self):
		self.s = QUdpSocket()
		self.s.bind(QHostAddress(szCurrentIP()),nUdpPort)
		self.s.readyRead.connect(self.receive)

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

	def __del__(self):
		self.s.close()

if __name__ == '__main__':
	import sys

	app = QtGui.QApplication(sys.argv)
	window = widgetUdp()
	window.resize(300,100)
	window.show()

	sys.exit(app.exec_())
