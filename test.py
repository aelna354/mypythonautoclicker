#Created for testing.
#The goal of this program: whenever CTRL is held while program is active,
#rapid fire print X.

from tkinter import *
import pyautogui
import keyboard
import time

class App(Frame):
	def __init__(self, master):
		Label(master,text="Press F1 or the start button, and we begin!").grid(row=0,column=0,sticky=W)
		Label(master,text="Press F2 or press stop, and we stop.").grid(row=1,column=0,sticky=W)
		keyboard.add_hotkey("F3", self.press)
	def press(self):
		time.sleep(0.3)
		print("Hi!")

program = Tk()
program.title("The test program")
program.geometry("400x250")
app = App(program)
program.mainloop()