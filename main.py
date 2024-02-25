from steam import Steam
from decouple import config
from tkinter import *

window = Tk("Hello")
window.geometry("500x500")


KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

user = steam.users.search_user("the12thchairman")
print(user)
window.mainloop()