import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")

from tkinter import *
from tkinter import ttk

class qgis(Frame):
    def __init__(self, master):
        super(qgis,self).__init__(master)
        months = ["Select a month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        items = ["Temperature", "Uwind", "Vwind", "Specific Humidity", "Surface Pressure", "Total Column Water Vapour", "Snow Depth", "Snowfall", "Relative Humidity", "Total Cloud Cover", "Wind Speed", "Solar Duration", "Pressure"]
        years = []
        days = []
        days.append("Select a day")
        years.append("Select a year")
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
        variableSecond.set("Select a day")
        self.daydrop2.grid(row = 1, padx = 495, pady = 15, sticky = "nw")
        variableFirst.set("Select a day")
        self.daydrop1.grid(row = 1, padx = 160, pady = 15, sticky = "nw")
        variable = StringVar(self.firstpage)
        self.firstdrop = OptionMenu(self.firstpage, variable, *months)
        variable.set("Select a month")
        self.firstdrop.grid(row = 1, padx = 70, pady = 45, sticky = "nw")
        self.dateL2 = Label(self.firstpage, justify = "left", text = "to", font = ("Arial", 10, "bold"), height = 1)
        self.dateL2.grid(row = 1, padx = 380, pady = 50, sticky = "nw")
        variable2 = StringVar(self.firstpage)
        self.secondrop = OptionMenu(self.firstpage, variable2, *years)
        variable2.set("Select a year")
        self.secondrop.grid(row=1, padx = 235, pady = 45, sticky = "nw")
        variable3 = StringVar(self.firstpage)
        self.thirdrop = OptionMenu(self.firstpage, variable3, *months)
        variable3.set("Select a month")
        self.thirdrop.grid(row = 1, padx = 400, pady = 45, sticky = "nw")
        variable4 = StringVar(self.firstpage)
        self.fourthdrop = OptionMenu(self.firstpage, variable4, *years)
        variable4.set("Select a year")
        self.fourthdrop.grid(row = 1, padx = 565, pady = 45, sticky = "nw")
        CheckVar1 = IntVar(self.firstpage)
        CheckVar2 = IntVar(self.firstpage)
        CheckVar3 = IntVar(self.firstpage)
        CheckVar4 = IntVar(self.firstpage)
        self.label3 = Label(self.firstpage, justify = "left", text = "Select the times: ", font = ("Arial", 10, "bold"), height = 1)
        self.C1 = Checkbutton(self.firstpage, text = "00:00:00", onvalue=1, offvalue=0, height=5, width=20, justify = "left")
        self.C2 = Checkbutton(self.firstpage, text = "06:00:00", onvalue=1, offvalue=0, height=5, width=20, justify = "left")
        self.C3 = Checkbutton(self.firstpage, text = "12:00:00", onvalue=1, offvalue=0, height=5, width=20, justify = "left")
        self.C4 = Checkbutton(self.firstpage, text = "18:00:00", onvalue=1, offvalue=0, height=5, width=20, justify = "left")
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
            values = [listbox1.get(idx) for idx in listbox1.curselection()]
            month1 = variable.get()
            year1 = variable2.get()
            month2 = variable.get()
            year2 = variable.get()
            zero = CheckVar1.get()
            six = CheckVar2.get()
            twelve = CheckVar3.get()
            eighteen = CheckVar4.get()
            print(values)
            
        self.button1 = Button(self.firstpage, justify = "center", text = "Get Data", command = lambda:getData(variable, variable2, variable3, variable4, CheckVar1, CheckVar2, CheckVar3, CheckVar4, listbox1, variableFirst, variableSecond), font = ("Arial", 10, "bold"), height = 1, width = 20)
        self.button1.grid(row = 1, padx = 400, pady = 250, sticky = "nw")
    
        
        

root = Tk()
root.title("QGIS Plugin Extension")
root.geometry("707x380")
visual = qgis(root)
root.mainloop()

