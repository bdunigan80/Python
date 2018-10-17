
    # Create your first GUI application

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Welcome to LikeGeeks app")

    # Setting the window Geometry
window.geometry('350x200')

rad1 = Radiobutton(window,text='First', value=1)

rad2 = Radiobutton(window,text='Second', value=2)

rad3 = Radiobutton(window,text='Third', value=3)

rad1.grid(column=0, row=0)

rad2.grid(column=1, row=0)

rad3.grid(column=2, row=0)


''' #Adding in a checkbutton widget
chk_state = BooleanVar()
chk_state.set(1) #Set check state
chk = Checkbutton(window, text='Choose', var=chk_state)
chk.grid(column=0, row=0)'''

''' #Setting up combox with item choices
combo = Combobox(window)

combo['values']= (1,2,3,4,5, "Text")
combo.current() #Set the selected item
combo.grid(column=0, row=0)
'''
'''   # Create a label widget

    # create a label using the label class
    # Setting the font and the text size
lbl = Label(window, text="Hello")

    # Set position of the form on the grid
lbl.grid(column=0, row=0)

#Getting user input with text box
txt = Entry(window,width=10)
# Put the textbox onto the grid
txt.grid(column=1, row=0)
txt.focus()


def clicked():
    #new_text = txt.get() # This will populate the "new_text" variable with the in put from the external txt variable
    lbl.configure(text=txt.get()) #Using this data call is faster and doesn't require you to set a variable with in this
    #function

    lbl.configure(text=txt.get())
    # Adding buttons widgets
btn = Button(window, text="click Me", command=clicked)
    # This is setting the button to the right of the "hello" text. The "hello" text is in a column of its own so we need
    # to make sure the button is not on top of the text.
btn.grid(column=2, row=0)

    # The last line which calls mainloop function, this function calls the endless loop of the window, so the window will
    # wait for any user interaction till we close it.'''


window.mainloop()



