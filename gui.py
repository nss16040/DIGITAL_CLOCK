from tkinter import Tk
from tkinter import Label
import time
root=Tk()
root.title("DIGITAL CLOCK")
def samay():
    display_samay=time.strftime("%I:%M:%S %p")
    d_clock.config(text=display_samay)
    d_clock.after(100,samay)
d_clock=Label(root,font=("Helvetica",90),bg="black",fg="white")
d_clock.pack()
samay()
root.mainloop()