from tkinter import *

class UI():
	def __init__(self):
		self.app = Tk()
		self.resolution = "600x480+0+0"
		self.width = 600
		self.length = 480

class Menu(UI):
	def __init__(self,width,length):
		super().__init__()
		self.resolution = "200x200+"+str(int(width/2-150))+"+"+str(int(length/2-100))
		self.changeResolution()
		self.__configure()
		self.__run = False

	def __configure(self):
		self.title = Label(self.app,text = "Menu")
		self.title.place(relx = 0.5,rely = 20/self.length, anchor = CENTER)
		self.closeButton = Button(self.app, text = "Close",command = self.app.destroy)
		self.closeButton.place(relx = 0.8,rely = 0.8, anchor = CENTER)
		self.runButton = Button(self.app, text = "Run",command=lambda: [self.toggleRun() & self.app.destroy()])
		self.runButton.place(relx = 0.2,rely = 0.8, anchor = CENTER)
		self.checkValues = IntVar()
		self.checkStonks = [None]*4
		self.checkStonks[0] = Radiobutton(self.app,text = "Microsoft",variable = self.checkValues,value=0)
		self.checkStonks[1] = Radiobutton(self.app,text = "Google",variable = self.checkValues,value=1)
		self.checkStonks[2] = Radiobutton(self.app,text = "Amazon",variable = self.checkValues,value=2)
		self.checkStonks[3] = Radiobutton(self.app,text = "Tesla",variable = self.checkValues,value=3)
		for i in range(4):
			self.checkStonks[i].place(relx = 0.2+i%2*0.5+i//4*0.3,rely = ((i//2)*80+100)/self.length,anchor = CENTER)

	def toggleRun(self):
		self.__run = True

	def run(self):
		return self.__run

	def getStonks(self):
		temp = self.checkValues.get()
		return temp

	def open(self):
		self.app.mainloop()

	def changeResolution(self):
		self.app.geometry(self.resolution)