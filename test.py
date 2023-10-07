import os

path = "C:\\Users\\matte\\OneDrive\\Desktop\\peppa.txt"

try:
    with open("tet.txt") as file:
        print(file.read())
except FileNotFoundError:
    print(":(")
 