import os

def line(l=100):
    for i in range(l):
        print("=",end="")
    print(" ")

def center(c=44):
    for i in range(c):
        print(" ",end="")
    
def cls():
    os.system("cls")
    
def pause():
    os.system("pause")
    
def myfun():
    ans=input()
    if ans == "2":
        return bool(ans)
    else:
        ans = 0
        return bool(ans)

cls()
line()
center(42)
print("|| BOOL ||")
line()

print("1+1= ",end="")
print(myfun())
line()
pause()

