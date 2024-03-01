from steam import Steam
from decouple import config
from tkinter import *

window = Tk("Hello")
window.geometry("500x500")

#gwiddy

username = Entry(window, width=50)
print(username)
username.pack()

def printinfo():
    user = steam.users.search_user(username)
    label = Label(window, text=user)
    label.pack()

confirm_button = Button(window, text="Confirm", command=printinfo)
confirm_button.pack()

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)


window.mainloop()