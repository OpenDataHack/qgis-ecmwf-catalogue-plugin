from __future__ import print_function
import os
from Loader import loader
from Qgis import qgis
from tkinter import *


if __name__ == "__main__":
	load = loader()
	root = Tk()
	root.title("QGIS Plugin Extension")
	root.geometry("707x380")
	visual = qgis(root, load)
	root.mainloop()

