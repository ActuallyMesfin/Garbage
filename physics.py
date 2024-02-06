from tkinter import *
from tkinter import ttk
import playsound


window = Tk()
window.title("THE MONEY GO WHERE I GO🔥")
window.geometry = "1000x1000"

def dumbass():
    print("FUCK")
    playsound.playsound("Vine boom.mp4")

stupidassfuckingbutton = Button(window, text="BRUH", command=dumbass)
stupidassfuckingbutton.pack()

window.mainloop()
