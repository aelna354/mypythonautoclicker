from tkinter import *
from tkinter import messagebox
import keyboard
import pyautogui
import webbrowser
import time
class App(Frame):
	def __init__(self, master):
		#we need the following:
		#active state
		#speed
		#left click, right click, or key?
		#if key, which one?
		#speed
		#enable hotkey (F1 by default)
		#disable key (F2 by default)
		self.master = master 	 	  #so other method can access it
		self.active = StringVar()	  #INACTIVE or ACTIVE (False or True)
		self.active.set("INACTIVE")
		self.speed = StringVar() 	  #how fast it is
		self.speed.set(".5") 		  #note: miliseconds is 1000 times
		self.enablekey = StringVar()  #enable hotkey
		self.enablekey.set("F3")
		self.disablekey = StringVar() #disable hotkey
		self.disablekey.set("F4")

		hyperlink = Label(master, text="Source Code", fg="blue", cursor="hand2")
		hyperlink.grid(row=1, column=0, sticky=W)
		hyperlink.bind("<Button-1>", lambda x: webbrowser.open_new(r"https://github.com/aelna354/mypythonautoclicker"))

		Button(master, text="Set Enable Hot Key",command=lambda:self.getcustomkey(0)).grid(row=2,column=0,sticky=W)
		enablekeybox = Entry(master,width=10,textvariable=self.enablekey)
		enablekeybox.configure(state='readonly')
		enablekeybox.grid(row=2,column=1,sticky=W)

		Button(master, text="Set Disable Hot Key", command=lambda:self.getcustomkey(1)).grid(row=3,column=0,sticky=W)
		disablekeybox = Entry(master,width=10,textvariable=self.disablekey)
		disablekeybox.configure(state='readonly')
		disablekeybox.grid(row=3,column=1,sticky=W)

		Label(master, text="Seconds between clicks").grid(row=4,column=0,sticky=W)
		Entry(master, textvariable=self.speed,width=10).grid(row=4,column=1,sticky=W)
		Button(master,text="Set Default",command=self.default).grid(row=5,column=0,sticky=W)

		self.status = Entry(master, textvariable=self.active, fg="red")
		self.status.configure(state="readonly")
		self.status.grid(row=6,column=0)

	def getcustomkey(self, num):
		if num == 0:
			keyval = keyboard.read_key()
			self.enablekey.set(keyval)
		if num == 1:
			keyval = keyboard.read_key()
			self.disablekey.set(keyval)

	def default(self):
		self.status["fg"] = "green"
		self.speed.set(".5")
		self.enablekey.set("F3")
		self.disablekey.set("F4")

program = Tk()
program.title("AutoClicker")
program.geometry("500x300")
app = App(program)
program.mainloop()
