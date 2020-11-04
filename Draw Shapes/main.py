import math

def promptShape():
    print("\n==================")
    print("First pick a shape")
    print("==================")

def promptDimensions():
    print("\n==========================")
    print("Second set your dimensions")
    print("==========================")

def calcCircle(radius):
    print("\n============================================")
    circum = int(2 * math.pi * radius)
    area = int(math.pi * (radius * radius))
    print("| The circumference of the circle is: ", circum, "     |")
    print("| The area of the circle is: ", area, "             |")
    print("============================================")

def calcSquare(side):
    print("\n==================================================")
    perimeter = int(side * 4)
    area = (side * side)
    print("| The perimeter of the square is: ", perimeter, "       |")
    print("| The area of the square is: ", area, "            |")
    print("==================================================")

run = True
print("\nHello, Welcome to the Shape Calculator")
print("Pick a shape and its dimensions and watch it be drawn out")
while run:
    promptShape()
    shape = str(input("\nEnter your shape: "))
    shape = shape.lower()
    if(shape == "circle"):
        promptDimensions()
        radius = int(input("\nEnter the radius of the circle: "))
        calcCircle(radius)
    if(shape == "square"):
        promptDimensions()
        side = int(input("\nEnter the side length of the square: "))
        calcSquare(side)
    if(shape == "rectangle"):
        pass
    if(shape != "circle" or "square" or "rectangle"):
        print("\nInvalid input")
    choice = input("Would you likes to continue? (Yes/No): ")
    choice = choice.lower()
    if(choice == "no"):
        print("\nGoodbye, and thanks for using the shape calculator!")
        run = False
