import os
from DownloadData import Downloader


class loader():
	
	def __init__(self):
		self.time=""
		self.date=""
		self.param=""
		self.target=""

	def testData(self):
		self.time="00"
		self.date="2013-09-01/to/2013-09-30"
		self.param="165.128/41.128"
		self.target="test1.grib"

	def downloadData(self):
		down = Downloader()
		down.downloadData(self.time, self.date, self.param, self.target)

#function that loads dictionary of types of data and it's IDs 
#example param: 'NameIDMap'
def loadNameIDMap(fileName):
	parentPath = os.path.abspath('..')
	s = open(parentPath+'/files/'+fileName, 'r')
	IDdict = dict()
	for line in s:
		print(line)
		splits = line.split(' ')
		print(splits)
		IDdict[splits[0]] = splits[1]
	for x in IDdict:
		print(x + " " + IDdict[x])




if __name__ == "__main__":
	load = loader()
	load.testData()
	load.downloadData()
