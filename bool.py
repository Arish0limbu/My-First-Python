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

cls()
line()
center(38)
print("|| Enter your details ||")
line()

print("Enter your name: ",end="")
name=input()
print("Enter your age: ",end="")
age=input()
line()
pause()

cls()
line()
center(42)
print("|| Your details ||")
line()
print("Name: "+name.title())
print("Age: ",age)
line()
pause()

cls()
line()
center(42)
print("|| Your details ||")
line()
print("Name:",bool(name))
print("Age: ",+bool(age),"\n# 1 Output means its true..")
line()
pause()

