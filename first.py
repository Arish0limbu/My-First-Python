import os


def cls():
    os.system("cls")


def line():
    for i in range(100):
        print("=", end="")
    print()


cls()
line()

print("Enter Your name: ", end="")
y = input()
y = y.title()

print("Enter your age: ", end="")
x = input()

line()
cls()
line()

print(y, "is your name.")
print(f"Your age is {x}")

line()
os.system("pause")