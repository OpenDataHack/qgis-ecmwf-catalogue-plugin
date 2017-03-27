from __future__ import print_function
import os
import time
from DownloadData import Downloader
import tempfile
import crayfish
import crayfish.plugin_layer
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface
from pop_up_dialog import PopUpDialog
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon


class loader():
	
	def __init__(self):
		self.tempDir = tempfile.gettempdir()
		self.timeStr=""
		self.date=""
		self.param=""
		self.target=""
		self.IDdict = dict()
		self.IDList = [141, 164, 166, 167, 137, 133, 46, 144, 157, 134, 165]


	def loadData(self, timeStr, date, param):
		print("show dialog")
		dlg = PopUpDialog("Loading data")
		dlg.show()
		print("is it up?")
		self.timeStr = timeStr
		self.date = date
		print(param) 
		for x in param:
			print(x)
			idNumber = self.IDList[x]
			self.param+=str(idNumber)+".128/"
		self.param = self.param[:-1]
		self.target=self.tempDir+"/downloadFile.grib"
		print(self.timeStr+" "+self.date+" "+self.param)
		dlg.label.setText("Downloading data")
		down = Downloader()
		down.downloadData(self.timeStr, self.date, self.param, self.target)
		dlg.changeText("Data is downloaded, displaying data ...")
		layer = crayfish.plugin_layer.CrayfishPluginLayer(self.tempDir+"/downloadFile.grib")
		QgsMapLayerRegistry.instance().addMapLayer(layer)
		dlg.changeText("Layer is displayed")
		time.sleep(3.5)


	def downloadData(self):
		if(self.timeStr==""):
			self.dlg.changeText("No time was selected")
		elif(self.param==[]):
			self.dlg.changeText("No parameters were selected")
		else:
			self.dlg.changeText("downloading data")
			time.sleep(5.5)
			down = Downloader()
			down.downloadData(self.timeStr, self.date, self.param, self.target)
			self.dlg.changeText("Data is downloaded, displaying data ...")
			layer = crayfish.plugin_layer.CrayfishPluginLayer(self.tempDir+"/downloadFile.grib")
			QgsMapLayerRegistry.instance().addMapLayer(layer)
			self.dlg.changeText("Layer is displayed")

