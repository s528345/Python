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
    circum = float(2 * math.pi * radius)
    area = float(math.pi * (radius * radius))
    print("The circumference of the circle is: ", circum)
    print("The area of the circle is: ", area)
    print("============================================")

def calcSquare(side):
    print("\n============================================")
    perimeter = int(side * 4)
    area = (side * side)
    print("The perimeter of the square is: ", perimeter)
    print("The area of the square is: ", area)
    print("============================================")

run = True
while run:
    print("\nHello, Welcome to the Shape Calculator")
    print("Pick a shape and its dimensions and watch it be drawn out")
    promptShape()
    shape = str(input("\nEnter your shape: "))
    shape = shape.lower()
    if(shape == "circle"):
        promptDimensions()
        radius = int(input("\nEnter the radius of the circle: "))
        calcCircle(radius)
    if(shape == "sqaure"):
        promptDimensions()
        side = int(input("\nEnter the side length of the square: "))
    else:
        print("Invalid input")
        choice = input("Would you likes to exit? ")
        choice.lower()
        if(choice == "yes"):
            run = False
        

