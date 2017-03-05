import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")

from Loader import loader
from tkinter import *
from tkinter import ttk

class qgis(Frame):
    def __init__(self, master, load):
        super(qgis,self).__init__(master)
        self.load = load
        months = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        items = ["2 meter Temperature", "10 meters Uwind", "10 meters Vwind", "Specific Humidity", "Surface Pressure", "Total Column Water Vapour", "Snow Depth", "Snowfall", "Relative Humidity", "Total Cloud Cover", "Solar Duration"]
        self.returnNum = ['snowDepth', 'totalCloudCover', '10mVwind', '2mTemperature', 'totalColumnWaterVapour', 'specificHumidity', 'solarDuration', 'snowfall', 'relativeHumidity', 'surfacePressure', '10mUwind']
        years = []
        days = []
        for i in range(1979, 2017, 1):
            years.append(i)
        for i in range(1, 32):
            days.append(i)
        self.grid()
        self.firstpage = Frame(self)
        self.firstpage.grid()
        self.titleL = Label(self.firstpage,justify = "center", text = "Data Loader", font = ("Arial", 30, "bold"), height = 1)
        self.titleL.grid(row = 0, padx = 260, pady = 0, sticky = "nw")
        self.dateL = Label(self.firstpage, justify = "left", text = "Enter a date: ", font = ("Arial", 10, "bold"), height = 1)
        self.dateL.grid(row = 1, padx = 0, pady = 50, sticky = "nw")
        variableFirst = StringVar(self.firstpage)
        self.daydrop1 = OptionMenu(self.firstpage, variableFirst, *days)
        variableSecond = StringVar(self.firstpage)
        self.daydrop2 = OptionMenu(self.firstpage, variableSecond, *days)
        variableSecond.set("1")
        self.daydrop2.grid(row = 1, padx = 495, pady = 15, sticky = "nw")
        variableFirst.set("1")
        self.daydrop1.grid(row = 1, padx = 160, pady = 15, sticky = "nw")
        variable = StringVar(self.firstpage)
        self.firstdrop = OptionMenu(self.firstpage, variable, *months)
        variable.set("1")
        self.firstdrop.grid(row = 1, padx = 70, pady = 45, sticky = "nw")
        self.dateL2 = Label(self.firstpage, justify = "left", text = "to", font = ("Arial", 10, "bold"), height = 1)
        self.dateL2.grid(row = 1, padx = 380, pady = 50, sticky = "nw")
        variable2 = StringVar(self.firstpage)
        self.secondrop = OptionMenu(self.firstpage, variable2, *years)
        variable2.set("1979")
        self.secondrop.grid(row=1, padx = 235, pady = 45, sticky = "nw")
        variable3 = StringVar(self.firstpage)
        self.thirdrop = OptionMenu(self.firstpage, variable3, *months)
        variable3.set("1")
        self.thirdrop.grid(row = 1, padx = 400, pady = 45, sticky = "nw")
        variable4 = StringVar(self.firstpage)
        self.fourthdrop = OptionMenu(self.firstpage, variable4, *years)
        variable4.set("1979")
        self.fourthdrop.grid(row = 1, padx = 565, pady = 45, sticky = "nw")
        CheckVar1 = IntVar(self.firstpage)
        CheckVar2 = IntVar(self.firstpage)
        CheckVar3 = IntVar(self.firstpage)
        CheckVar4 = IntVar(self.firstpage)
        self.label3 = Label(self.firstpage, justify = "left", text = "Select the times: ", font = ("Arial", 10, "bold"), height = 1)
        self.C1 = Checkbutton(self.firstpage, variable = CheckVar1, text = "00:00:00", onvalue=1, offvalue=0, height=5, width=20, justify = "left")
        self.C2 = Checkbutton(self.firstpage, variable = CheckVar2, text = "06:00:00", onvalue=1, offvalue=0, height=5, width=20, justify = "left")
        self.C3 = Checkbutton(self.firstpage, variable = CheckVar3, text = "12:00:00", onvalue=1, offvalue=0, height=5, width=20, justify = "left")
        self.C4 = Checkbutton(self.firstpage, variable = CheckVar4, text = "18:00:00", onvalue=1, offvalue=0, height=5, width=20, justify = "left")
        self.label3.grid(row = 1, padx = 0, pady = 105, sticky = "nw")
        self.C1.grid(row = 1, padx = 90, pady=70, sticky = "nw")
        self.C2.grid(row = 1, padx = 190, pady=70, sticky = "nw")
        self.C3.grid(row = 1, padx = 290, pady=70, sticky = "nw")
        self.C4.grid(row = 1, padx = 390, pady=70, sticky = "nw")
        listbox1 = Listbox(self.firstpage, selectmode=MULTIPLE, width = 30)
        self.label4 = Label(self.firstpage, justify = "left", text = "Select the data: ", font = ("Arial", 10, "bold"), height = 1)
        self.label4.grid(row = 1, padx = 0, pady = 150, sticky = "nw")
        for item in items:
            listbox1.insert(END, item)
        listbox1.grid(row = 1, padx = 90, pady = 150, sticky = "nw")
        def getData(variable, variable2, variable3, variable4, CheckVar1, CheckVar2, CheckVar3, CheckVar4, listbox1, variableFirst, variableSecond):
            values = [self.returnNum[idx] for idx in listbox1.curselection()]
            if(int(variable.get()) < 10):
                month1 ="0"
            month1 += variable.get()
            year1 = variable2.get()
            if(int(variableFirst.get()) <10):
                day1 ="0"
            day1 += variableFirst.get()
            if(int(variable3.get()) < 10):
                month2 ="0"
            month2 += variable3.get()
            year2 = variable4.get()
            if(int(variableSecond.get()) <10):
                day2 ="0"
            day2 += variableSecond.get()
            times = CheckVar1.get()+CheckVar2.get()+CheckVar3.get()+CheckVar4.get()
            print(values)
            #calculating time from checkbox and putting it into right format
            time=""
            if(CheckVar1.get()):
                time+="00/"
            if(CheckVar2.get()):
                time+="06/"
            if(CheckVar3.get()):
                time+="12/"
            if(CheckVar4.get()):
                time+="18/"
            time = time[:-1]
            date = year1+"-"+month1+"-"+day1+"/to/"+year2+"-"+month2+"-"+day2
            print(time)
            print(date)
            load.loadData(time, date, values)
            load.downloadData()
            
        self.button1 = Button(self.firstpage, justify = "center", text = "Get Data", command = lambda:getData(variable, variable2, variable3, variable4, CheckVar1, CheckVar2, CheckVar3, CheckVar4, listbox1, variableFirst, variableSecond), font = ("Arial", 10, "bold"), height = 1, width = 20)
        self.button1.grid(row = 1, padx = 400, pady = 250, sticky = "nw")
    
        
       

