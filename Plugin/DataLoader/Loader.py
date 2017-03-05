from __future__ import print_function
import os
from DownloadData import Downloader
import tempfile
import crayfish
import crayfish.plugin_layer
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface


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
		if(self.time==""):
			print("No time was selected")
		elif(self.param==[]):
			print("No parameters were selected")
		else:
			down = Downloader()
			down.downloadData(self.time, self.date, self.param, self.target)
			print("data is downloaded")
			layer = crayfish.plugin_layer.CrayfishPluginLayer(self.tempDir+"/downloadFile.grib")
			QgsMapLayerRegistry.instance().addMapLayer(layer)
			print("layer displayed")

