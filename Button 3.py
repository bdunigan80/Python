#Project: Guui Window with three buttons
#Creator: Brian Dunigan
#Creation date: 10-13-2018

from tkinter import *

class Application(Frame):
    #"""A GUI Application with three buttons."""

    def __init__(self, master):
        #This will initialise the frame'''
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0 #Count the number of button clicks
        self.create_widgets()

    def create_widgets(self):

    #Create  button which displays number of clicks

      self.button1 = Button(self, text = "First Button")
      self.button1.grid()

root = Tk()

root.title("Buttons..ohmy!")
root.geometry("300x300")

app = Application(root)

root.mainloop()