from rich import print

f = open("./input2", "r")
answer=0

pos=0
list=[None] * 4
for l in f:
    l=int(l)
    list[pos%4]=l
    if pos >= 4:
        a= list[(pos-3)%4] + list[(pos-2)%4] + list[(pos-1)%4]
        b= list[(pos-2)%4] + list[(pos-1)%4] + list[(pos)%4]
        if a < b:
            answer +=1

    pos +=1
print(answer)