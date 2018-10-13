from tkinter import *





class Application(Frame):
    #"""A GUI Application with three buttons."""

    def __init__(self, master):
        '''This will initialise the frame'''

        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
    #""" Create 3 buttons that do nothing"""
    #Create the first button
      self.button1 = Button(self, text = "First Button")
      self.button1.grid()

    # Second button

      self.button2 = Button(self)
      self.button2.grid()
      self.button2.configure(text = "Second Button")

    #create 3rd button

      self.button3 = Button(self)
      self.button3.grid()
      self.button3["text"]= "Third Button"

root = Tk()

root.title("Buttons..ohmy!")
root.geometry("300x300")

app = Application(root)

root.mainloop()


