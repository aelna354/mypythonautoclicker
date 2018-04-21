#Created for testing. The programmer's equivalent of scrap paper... #philosophicalprogrammer
#This program can be toggled with F3 regardless of window focus.
#When enabled, the program will periodically print "Yay!"

from tkinter import * #gui
import pyautogui	  #clicker
import keyboard		  #hotkeys

class App(Tk):
	def __init__(self, master):
		self.master = master #used so another method can access master
		self.active = False

		Label(master, text="Press F3 and we begin!").grid(row=0,column=0,sticky=W)
		Label(master, text="Press F4 and we stop!").grid(row=1,column=0,sticky=W)

		keyboard.add_hotkey("F3", self.enable)
		keyboard.add_hotkey("F4", self.disable)

	def start(self):
		if self.active:
			print("Yay!")
			self.master.after(10, self.start)

	def enable(self):
		if not self.active:
			self.active = True
			self.start()
	
	def disable(self):
		if self.active:
			self.active = False
			print("Done.")

program = Tk()
program.title("The test program")
program.geometry("400x250")
app = App(program)
program.mainloop()