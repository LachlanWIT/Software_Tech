# Building Gui using TKinter https://realpython.com/python-gui-tkinter/

import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkcalendar
from datetime import timedelta


# this is a function which returns the selected combo box item
def getSelectedComboItem():
    return comboOneTwoPunch.get()


def date_range(start, stop):
    global dates  # If you want to use this outside of functions

    dates = []
    diff = (stop - start).days
    for i in range(diff + 1):
        day = start + timedelta(days=i)
        dates.append(day)
    if dates:
        print(dates)  # Print it, or even make it global to access it outside this
    else:
        print('Make sure the end date is later than start date')


window = Tk()

# This is the section of code which creates the main window
window.geometry('800x800')
window.configure(background='#808080')
window.title("Analysis Tool")

# This is the section of code which creates a button
button = tk.Button(window, text='Close', width=25, bg='#C1CDCD', font=('arial', 12, 'normal'),
                   command=window.destroy).place(x=550, y=750)

# This is the section of code which creates a combo box
comboOneTwoPunch = ttk.Combobox(window, values=['All (default)', 'Search', 'insight', 'analysis', '*fucking missing*'],
                                font=('arial', 12, 'normal'), width=10)
comboOneTwoPunch.place(x=50, y=50)
comboOneTwoPunch.current(1)

# First, we create a canvas to put the picture on
worthAThousandWords = Canvas(window, height=48, width=48)
# Then, we actually create the image file to use (it has to be a *.gif)
picture_file = PhotoImage(
    file='logo.gif')  # <-- you will have to copy-paste the filepath here, for example 'C:\Desktop\pic.gif'
# Finally, we create the image on the canvas and then place it onto the main window
worthAThousandWords.create_image(48, 0, anchor=NE, image=picture_file)
worthAThousandWords.place(x=375, y=50)

date1 = tkcalendar.DateEntry(window)
date1.place(x=550, y=50)

date2 = tkcalendar.DateEntry(window)
date2.place(x=650, y=50)

Button(window, text='Find range', command=lambda: date_range(date1.get_date(), date2.get_date())).pack()

window.mainloop()
