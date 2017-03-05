import os
from Loader import loader
from Qgis import qgis

if __name__ == "__main__":
	load = loader()
	load.testEntry1()
	root = Tk()
	root.title("QGIS Plugin Extension")
	root.geometry("707x380")
	visual = qgis(root, load)
	root.mainloop()

