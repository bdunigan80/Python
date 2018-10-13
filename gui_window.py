from tkinter import *

root = Tk()

root.title("GUI You")
root.geometry("500x300")

app = Frame(root)
app.grid()
button1 = Button(app, text = "Start")
button1.grid()


button2 = Button(app)
button2.grid()

button2.configure(text ="OK")

button3 = Button(app)
button3.grid()
button3["text"] = "Stopl"

root.mainloop()