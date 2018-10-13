#Project: Guui Window with three buttons
#Creator: Brian Dunigan
#Creation date: 10-13-2018

from tkinter import *

class Application(Frame):
    #"""A GUI Application with three buttons."""

    def __init__(self, master):
        #This will initialise the frame

        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
    #Create 3 buttons that do nothing

    #Create the first button
      self.button = Button(self)
      self.button.["text"] = "Total Clicks: 0"
      self.button["command"] = self.update_count
      self.button.grid()

    def update_count(self):
        #Increase the click count and display the new totlal
        self.button_clicks + 1
        self.button["text"] "Total Clicks: " + str(self.button_clicks)

root = Tk()

root.title("Buttons..ohmy!")
root.geometry("300x300")

app = Application(root)

root.mainloop()


