#App for being an autoclicker. Created for and by aelna354.


from tkinter import *
import keyboard, webbrowser, mouse
#keyboard is from: https://github.com/boppreh/keyboard
#mouse is from: https://github.com/boppreh/mouse

class App(Frame):
	def __init__(self, master):
		self.master = master #so that another method to access it
		self.active = StringVar()
		self.active.set("INACTIVE")
		self.speed = IntVar()
		self.speed.set(25)

		hyperlink = Label(master, text="Source Code", fg="blue", cursor="hand2")
		hyperlink.grid(row=1, column=0, sticky=W)
		hyperlink.bind("<Button-1>", lambda x: webbrowser.open_new(r"https://github.com/aelna354/mypythonautoclicker"))

		Label(master, text="Seconds between clicks").grid(row=2,column=0,sticky=W)

		speedframe = Frame()
		speed = [.025, .05, .25, .5, 1]
		for pos, i in enumerate(speed):
			Radiobutton(speedframe, text=i, variable=self.speed, value=int(i*1000)).grid(row=0,column=pos)
		speedframe.grid(row=2,column=1,sticky=W)

		self.status = Entry(master, textvariable=self.active, fg="red")
		self.status.configure(state="readonly")
		self.status.grid(row=3,column=0,sticky=W)

		Label(master, fg="black", bg="silver",
		text="Press either F3 or F4 to toggle the program.\n"+
		"You can also stop the program with the RMB.\nNOTE: You cannot"+
		" change speed while program is active."
		).grid(row=4,column=0,columnspan=3,sticky=W)

		keyboard.add_hotkey("F3", self.toggle)
		keyboard.add_hotkey("F4", self.toggle)
		mouse.on_button(self.stop, buttons='right')

	def toggle(self):
		if self.active.get() == "ACTIVE":
			self.stop()
		else:
			self.activate()

	def activate(self):
		if self.active.get() == "INACTIVE":
			#We set true speed once so speed won't change while running
			self.truespeed = self.speed.get()
			self.active.set("ACTIVE")
			self.status["fg"] = "green"
			self.start()

	def start(self):
		if self.active.get() == "ACTIVE":
			mouse.click()
			self.master.after(self.truespeed, self.start)

	def stop(self):
		if self.active.get() == "ACTIVE":
			self.active.set("INACTIVE")
			self.status["fg"] = "red"

program = Tk()
program.title("AutoClicker")
program.geometry("390x130")
app = App(program)
program.mainloop()
