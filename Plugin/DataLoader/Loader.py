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


class loader():
	
	def __init__(self):
		self.tempDir = tempfile.gettempdir()
		self.time=""
		self.date=""
		self.param=""
		self.target=""
		self.IDdict = dict()
		self.IDList = [141, 164, 166, 167, 137, 133, 46, 144, 157, 134, 165]


	def loadData(self, time, date, param):
		self.time = time
		self.date = date
		print(param) 
		for x in param:
			print(x)
			idNumber = self.IDList[x]
			self.param+=str(idNumber)+".128/"
		self.param = self.param[:-1]
		self.target=self.tempDir+"/downloadFile.grib"
		print(self.time+" "+self.date+" "+self.param)


	def downloadData(self):
		self.dlg = PopUpDialog("Your choices are beeing processed ...")
		self.dlg.show()
		print("Showing dialog")
		if(self.time==""):
			self.dlg.changeText("No time was selected")
		elif(self.param==[]):
			self.dlg.changeText("No parameters were selected")
		else:
			self.dlg.changeText("downloading data")
			down = Downloader()
			down.downloadData(self.time, self.date, self.param, self.target)
			self.dlg.changeText("Data is downloaded, displaying data ...")
			layer = crayfish.plugin_layer.CrayfishPluginLayer(self.tempDir+"/downloadFile.grib")
			QgsMapLayerRegistry.instance().addMapLayer(layer)
			self.dlg.changeText("Layer is displayed")
		time.sleep(12.5)

