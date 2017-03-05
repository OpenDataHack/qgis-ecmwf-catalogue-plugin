import os
from DownloadData import Downloader

class loader():
	
	def __init__(self):
		self.parentDir = os.path.abspath('..')
		self.time=""
		self.date=""
		self.param=""
		self.target=""
		self.IDdict = dict()
		self.loadNameIDMap('NameIDMap')

	def testData(self):
		self.time="00"
		self.date="2013-09-01/to/2013-09-30"
		self.param="165.128/41.128"
		self.target=self.parentDir+'/files/test1.grib'

	def testEntry1(self):
		self.loadData("00/12", "2013-08-01/to/2013-10-01", ["10mUwind","10mVwind"])
		self.setFileName("testEntry1")
		print(self.time)
		print(self.date)
		print(self.param)
		print(self.target)
		self.downloadData()


	def loadData(self, time, date, param):
		self.time = time
		self.date = date
		for x in param:
			print(x)
			idNumber = self.IDdict[x].rstrip()	#.rstrip() is for removing newline character that is appended at the end of string
			self.param+=idNumber+".128/"
		self.param = self.param[:-1]
		self.setFileName("name1")

	def setFileName(self, name):
		self.target=self.parentDir+'/files/'+name+".grib"


	def downloadData(self):
		down = Downloader()
		down.downloadData(self.time, self.date, self.param, self.target)

	#function that loads dictionary of types of data and it's IDs 
	#example param: 'NameIDMap'
	def loadNameIDMap(self, fileName):
		s = open(self.parentDir+'/files/'+fileName, 'r')
		for line in s:
			#print(line)
			splits = line.split(' ')
			#print(splits)
			self.IDdict[splits[0]] = splits[1]
		#print (self.IDdict.keys())
