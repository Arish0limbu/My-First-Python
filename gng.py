import os

def line(c=100):
    for i in range(c):
        print("=",end="")
    print(" ")

def center(c=45):
    for i in range(c):
        print(" ",end="")

def cls():
    os.system("clear")

def pause():
    os.system("pause")
        
def head(c=45):
    cls()
    line()
    center(c)

head()
print("Enter your details")
line()

print("Enter your name: ",end="")
name = input()
line()
pause()

head(43)
print("|| Checking ||")
line()

if 'a' not in name or 'A' not in name:
    print(name.title(),"Verified.....")
else:
    print("No one verified..........")
line()
