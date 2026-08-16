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
line()
print(y.upper(),"is your name.")
