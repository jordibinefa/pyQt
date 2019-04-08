#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
wellproArduino07.py

20160428
"""

import sys
from PyQt4 import Qt, QtGui, QtCore
from ui_wellproArduino07 import Ui_wellproArduino
import serial
from time import sleep
from crc16b import calcByte,calcString,hexCRC,checkModbusWithCrc,readHex

class WellPro(QtGui.QWidget, Ui_wellproArduino):
	def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
		QtGui.QWidget.__init__(self, parent, f)
		self.setupUi(self)
		
		port='/dev/ttyUSB0'
		baudrate = 9600
		self.ser = serial.Serial(
			port,
			baudrate,
			timeout=0,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_TWO,
			bytesize=serial.EIGHTBITS
		)
		self.pixmapGris = QtGui.QPixmap("imatges/gris.png")
		self.pixmapVermell = QtGui.QPixmap("imatges/vermell.png")
		self.pixmapS4A = QtGui.QPixmap("imatges/s4a.png")
		self.labelBit0.setPixmap(self.pixmapGris)
		self.labelBit1.setPixmap(self.pixmapGris)
		self.labelBit2.setPixmap(self.pixmapGris)
		self.labelBit3.setPixmap(self.pixmapGris)
		self.label_2.setPixmap(self.pixmapS4A)
		self.temporitzador = QtCore.QTimer()
		self.connect(self.temporitzador, Qt.SIGNAL("timeout()"), self.funcioTemporitzada)
		self.temporitzador.start(100)
		self.connect(self.btEscr, QtCore.SIGNAL("clicked()"), self.funcEscriptura)		
		self.connect(self.btLect, QtCore.SIGNAL("clicked()"), self.funcLectura)		
		
		self.temporitzadorTrama = QtCore.QTimer()
		self.connect(self.temporitzadorTrama, Qt.SIGNAL("timeout()"), self.funcioTmpTrama)
		#self.temporitzadorTrama.start(500)
		self.connect(self.btTmp, QtCore.SIGNAL("clicked()"), self.ctrlTmpTrama)
		self.btTmpPremut = 0
		self.bRW = 0	

	def processa(self,sz,nQ):
		#print "Rebut:\n",sz
		print "He rebut %d bytes" % nQ
		readHex(sz)
		print ""
		if ord(sz[1]) == 0x02:
			print "Lectura reconeguda"
			self.vInterpretaLecturaModbus(sz,nQ)		
		if ord(sz[1]) == 0x0F:
			print "Escriptura reconeguda"

	def vInterpretaLecturaModbus(self,sz,nQ):
		#print "bit 0 (botó 2): ",
		if ord(sz[3]) & 0x01:
			#print "HIGH"
			self.labelBit0.setPixmap(self.pixmapVermell)
		else:
			#print "LOW"	
			self.labelBit0.setPixmap(self.pixmapGris)			
		if ord(sz[3]) & 0x02:
			self.labelBit1.setPixmap(self.pixmapVermell)
		else:
			self.labelBit1.setPixmap(self.pixmapGris)			
		if ord(sz[3]) & 0x04:
			self.labelBit2.setPixmap(self.pixmapVermell)
		else:
			self.labelBit2.setPixmap(self.pixmapGris)			
		if ord(sz[3]) & 0x08:
			self.labelBit3.setPixmap(self.pixmapVermell)
		else:
			self.labelBit3.setPixmap(self.pixmapGris)			

	def funcioTemporitzada(self):
		data = self.ser.read(1)
		n = self.ser.inWaiting()
		if n:
			data = data + self.ser.read(n)
		if len(data):
			self.processa(data,n)

	def funcioTmpTrama(self):
		if self.bRW:
			self.bRW = 0
			self.funcEscriptura()
		else:
			self.bRW = 1
			self.funcLectura()

	def ctrlTmpTrama(self):
		if self.btTmpPremut:
			self.btEscr.setEnabled(1);
			self.btLect.setEnabled(1);
			self.btTmp.setText("Tmp ON")
			self.btTmpPremut = 0			
			self.temporitzadorTrama.stop()
		else:
			ms = self.lineEdit_ms.text()
			n_ms = int(str(ms))
			if n_ms >= 200:
				self.temporitzadorTrama.start(n_ms)
				self.btEscr.setEnabled(0);
				self.btLect.setEnabled(0);
				self.btTmp.setText("Tmp OFF")
				self.btTmpPremut = 1
			
	def __del__(self):
		self.ser.close()

	def funcCalculaByteEscriptura(self):
		by = 0x00;
		if self.checkBoxBit0.isChecked():
			by |= 0x01
		if self.checkBoxBit1.isChecked():
			by |= 0x02
		if self.checkBoxBit2.isChecked():
			by |= 0x04
		if self.checkBoxBit3.isChecked():
			by |= 0x08
		return by

	def funcEscriptura(self):
		st = self.lineEdit.text()
		nCmpt = 0
		st = ""
		stMB = ""
		for ch in self.lineEdit.text():
			st += ch
			nCmpt = nCmpt + 1
			if nCmpt == 2:
				nSt = int(str(st),16)
				stMB+="%c"%(nSt)
				nCmpt = 0
				st = ""
		#01 0F 00 00 00 08 01 A4 FF 2E
		stMB+="%c%c%c%c%c%c%c"%(0x0F,0x00,0x00,0x00,0x08,0x01,self.funcCalculaByteEscriptura())
		hCRC = hexCRC(stMB)
		addedCRC="%c%c"%(hCRC>>8,hCRC&0xFF)
		szAddedCRC="%2X%2X"%(hCRC>>8,hCRC&0xFF)
		stMB += addedCRC
		readHex(stMB)
		print ""
		self.ser.write(stMB)

	def funcLectura(self):
		st = self.lineEdit.text()
		nCmpt = 0
		st = ""
		stMB = ""
		for ch in self.lineEdit.text():
			st += ch
			nCmpt = nCmpt + 1
			if nCmpt == 2:
				nSt = int(str(st),16)
				stMB+="%c"%(nSt)
				nCmpt = 0
				st = ""
		#01 0F 00 00 00 08 01 A4 FF 2E
		stMB+="%c%c%c%c%c"%(0x02,0x00,0x00,0x00,0x08)
		hCRC = hexCRC(stMB)
		addedCRC="%c%c"%(hCRC>>8,hCRC&0xFF)
		szAddedCRC="%2X%2X"%(hCRC>>8,hCRC&0xFF)
		stMB += addedCRC
		readHex(stMB)
		print ""
		self.ser.write(stMB)

if __name__ == '__main__':

	app = QtGui.QApplication(sys.argv)
	window = WellPro()
	window.show()

	sys.exit(app.exec_())
