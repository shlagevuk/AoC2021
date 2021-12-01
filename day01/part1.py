from rich import print

f = open("./input1", "r")
answer=0
p = None
for l in f:
    l=int(l)
    if p is None:
        print("N/A")
    else:
        if l > p :
            print("increase")
            answer+=1
        else:
            print("decrease")  
    p=l 

print(answer)