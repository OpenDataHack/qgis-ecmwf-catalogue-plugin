from __future__ import print_function
from ecmwfapi import ECMWFDataServer

class Downloader():

	def __init__(self):
		self.server = ECMWFDataServer()

	#function that downloads data
	#@params:
	#time -> defines time period, written in format "00:00:00/06:00:00/12:00:00/18:00:00" , or just "00"
	#date -> "2013-09-01/to/2013-09-30"
	#param -> parameters of data downloaded - in format: "165.128/41.128" , .128 stands for source of data - main, naming list http://apps.ecmwf.int/codes/grib/param-db
	#target - route to file where to save data, should have .grib in fromat: "testingData.grib"
	def downloadData(self, time, date, param, target):
		self.server.retrieve({
		    'dataset' : "interim",
		    'time'    : time,
		    'date'    : date,
		    'step'    : "0",
		    'type'    : "an",
		    'levtype' : "sfc",   
		    'param'   : param,		 
		    'grid'    : "0.75/0.75",
		    'target'  : target		
		    })
