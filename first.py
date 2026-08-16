import os

def cls():
        os.system("cls")

def line():
        for i in range(100):
            print("=",end="")
        print(" ")
        
cls()
line()
print("Enter Your name: ",end="")
y=input()
print("Enter your age: ",end="")
x=input()
line()
cls()
print(y.upper(),"is your name.")
z=f"Your age is {x}"
print(z)
