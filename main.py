from tkinter import *
import pyautogui
import time
import webbrowser

class App(Frame):
	def __init__(self, master):
		self.interval = StringBar()
		self.interval.set(0.4)

		Radiobutton(master, text="Slow (1 second)", variable=self.interval, value = 1).grid(row=0,column=0)
		Radiobutton(master, text="Medium (.7 second)", variable=self.interval, value = .7).grid(row=0,column=1)
		Radiobutton(master, text="Fast (.4 second)", variable=self.interval, value = .7).grid(row=0,column=2)

		Label(master, text="Custom speed").grid(row=1, column=0)
		Entry(master,width=55, textvariable)

		Button(master, text="Start (Hotkey F2)", command=self.begin()).grid(row=1,column=0)
		Button(master, text="Stop (Hotkey F2)", command=self.stop()).grid(row=2,column=0)
	def start(self):
		pyautogui.press('space')

program = Tk()
program.title("Space AutoClicker")
program.geometry("500x300")
app = App(program)
program.mainloop()
