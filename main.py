#credits to https://github.com/boppreh/keyboard and https://github.com/boppreh/mouse
#App for being an autoclicker.

from tkinter import *
from tkinter import messagebox
import keyboard
import webbrowser
import mouse

class App(Frame):
	def __init__(self, master):
		self.master = master #here to allow another method to access it
		self.active = StringVar() #determines if program should be autoclicking
		self.active.set("INACTIVE")
		self.speed = IntVar() #miliseconds between autoclicks
		self.speed.set(500)

		hyperlink = Label(master, text="Source Code", fg="blue", cursor="hand2")
		hyperlink.grid(row=1, column=0, sticky=W)
		hyperlink.bind("<Button-1>", lambda x: webbrowser.open_new(r"https://github.com/aelna354/mypythonautoclicker"))

		Label(master, text="Seconds between clicks").grid(row=2,column=0,sticky=W)

		speedframe = Frame()
		speed = [.1, .25, .5, 1, 1.25, 2]
		for pos, i in enumerate(speed):
			Radiobutton(speedframe, text=i, variable=self.speed, value=int(i*1000)).grid(row=0,column=pos)
		speedframe.grid(row=2,column=1,sticky=W)

		self.status = Entry(master, textvariable=self.active, fg="red")
		self.status.configure(state="readonly")
		self.status.grid(row=3,column=0)

		actionframe = Frame()
		Button(actionframe, text="Start (F3)", width=15, bg="silver", fg="green", command=self.activate).grid(row=0,column=0,sticky=W)
		Button(actionframe, text="Stop (F4, RMB)", width=15, bg="silver", fg="red", comman=self.stop).grid(row=0,column=1,sticky=W)
		actionframe.grid(row=4,column=1,sticky=W)

		keyboard.add_hotkey("F3", self.activate)
		keyboard.add_hotkey("F4", self.stop)
		mouse.on_button(self.stop, buttons='right')

		Button(master, text="How To Use", command=lambda:self.help()).grid(row=5,column=0,sticky=W)

	def activate(self):
		if not (self.active.get() == "ACTIVE"):
			#we don't want to change speed WHILE active so we set it once
			self.truespeed = self.speed.get()
			self.active.set("ACTIVE")
			self.status["fg"] = "green"
			self.start()

	def start(self):
		if self.active.get() == "ACTIVE":
			mouse.click()
			print("Click.") #for debugging
			self.master.after(self.truespeed, self.start)

	def stop(self):
		if self.active.get() == "ACTIVE":
			self.active.set("INACTIVE")
			self.status["fg"] = "red"
			print("Done.")

	def help(self):
		messagebox.showinfo("Hi!","Select how many seconds are between clicks."+
							" (For example, with 0.5, you have a half second between clicks, or two clicks a second.)\n"+
							"To enable clicking, either press F3 or hit the Start button.\n"+
							"To disable, either hit the RMB, press F4, or hit the Stop button.\n\n"+
							"(NOTE: You cannot change the speed while the program is active. You must first disable it before changing speed.)\n")

program = Tk()
program.title("AutoClicker")
program.geometry("400x150")
app = App(program)
program.mainloop()
