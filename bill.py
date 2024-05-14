import tkinter
mainWindow = tkinter.Tk()

mainWindow.title("Lista cumparaturi")
mainWindow.geometry('640x480')
def increase(n):
    n=n+1
l={'mere':5,'pere':7,'portocale':9,'mandarine':10,'lamai':10,'rosii':8,'castraveti':9,'ardei':8,'ceapa':6}
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
label = tkinter.Label(mainWindow, text="Ce doresti sa cumperi ?")
label.grid(row=0, column=0)
r=tkinter.Listbox(mainWindow)
r.grid(row=1,column=0,sticky='nsew')
r.config(border=1)
for x in l.keys():
 r.insert(tkinter.END,x)
leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)



rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2)
button1 = tkinter.Button(rightFrame, text="mere",command=increase(a))
button2 = tkinter.Button(rightFrame, text="pere",command=increase(b))
button3 = tkinter.Button(rightFrame, text="portocale",command=increase(c))
button4 = tkinter.Button(rightFrame, text="mandarine",command=increase(d))
button5 = tkinter.Button(rightFrame, text="lamai",command=increase(e))
button6 = tkinter.Button(rightFrame, text="rosii",command=increase(f))
button7 = tkinter.Button(rightFrame, text="castraveti",command=increase(g))
button8 = tkinter.Button(rightFrame, text="ardei",command=increase(h))
button9 = tkinter.Button(rightFrame, text="ceapa",command=increase(i))
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=3, column=0)
button5.grid(row=4, column=0)
button6.grid(row=5, column=0)
button7.grid(row=6, column=0)
button8.grid(row=7, column=0)
button9.grid(row=8, column=0)



mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
mainWindow.mainloop()
