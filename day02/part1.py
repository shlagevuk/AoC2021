import math 
d=0
f=0
for line in open("./input","r"):
    a,b = str.split(line)
    if a == "forward":
        f += int(b)
    elif a == "up":
        d -= int(b)
    elif a == "down":
        d += int(b)

print(f*d)