import os

os.system("cls")

name = ["ram", "shyam", "hari"]
fruit = list(
    ("apple", "banana", "mango", "cherry", "melon", "papaya")
)  # List can also write as list((.........))

print(name)
print(fruit[0])

fruit[0] = "Lemon"
fruit.insert(0, "apple")
print(fruit[0:5])

name.extend(fruit)

print(name)
