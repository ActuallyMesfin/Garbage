from steam import Steam
from decouple import config

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

user = steam.users.search_user("the12thchairman")
print(user)
#I FUCKING HATE SATURDAYS