import math

print("==================")
print("Area Calculator 📐")
print("==================")
print("1) Triangle") 
print("2) Rectangle") 
print("3) Square")
print("4) Circle")
print("5) Quit")

shape = int(input("Which shape: "))

if shape == 3:
  side = float(input("Side: "))
  area = side ** 2
  print(f"The area is {area}")
elif shape == 2:
  length = float(input("Length: "))
  width = float(input("Width: "))
  area = length * width
  print(f"The area is {area}")
elif shape == 1:
  base = int(input("Base: "))
  height = int(input("Height: "))
  area = (height * base) / 2
  print(f"The area is {area}")
elif shape == 4:
  radius = int(input("Radius:"))
  area = math.pi * (radius ** 2)
  print(f"The area is {area}")
elif shape == 5:
    print("Goodbye!")
else:
    print("Invalid selection. Please choose 1-5.")
