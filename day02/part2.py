aim=0
d=0
f=0
for line in open("./input","r"):
    a,b = str.split(line)
    if a == "forward":
        f += int(b)
        d += int(b)*aim
    elif a == "up":
        aim -= int(b)
    elif a == "down":
        aim += int(b)

print(f*d)