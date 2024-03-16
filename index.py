import random

list = {"123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
code = "XXXX-XXXX-XXXX"

x = len(code)
for i in range(0, x):
    code[x] = random.choice(list)
    x+=1

print(code)
