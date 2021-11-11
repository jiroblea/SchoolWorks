# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms 
# Laboratory Exercise No. 1

import math
from typing import Type

def line():
    return "-----------------------"

# Problem 1
# Create a program that will add, subtract, multiply and divide two numbers.
# - Use user defined function for each operator
# - Any number divided by zero will result to undefined
# - Use int data type only for all variables declared

def basic_math_operations():
    def addition(num1: int, num2: int) -> int:
        return num1 + num2

    def subtraction(num1: int, num2: int) -> int:
        return num1 - num2

    def multiplication(num1: int, num2: int) -> int:
        return num1 * num2

    def division(num1: int, num2: int): 
        try:
            return round(num1 / num2, 2)
        except ZeroDivisionError:
            return "undefined!"

    def ask_number_input() -> tuple:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("The program only accept integers.")

    def display_output(result_name: str, fnctn) -> None:
        try:
            num = ask_number_input()
            if fnctn == division and num[1] == 0:
                print("Undefined!")
            else:
                print(f"The {result_name} is", fnctn(num[0], num[1]))
        except:
            print("Try again.")

    while True:
        print("\n***********************\nMENU\n***********************")
        print("[A] - addition") 
        print("[S] - subtraction")
        print("[M] - multiplication")
        print("[D] - division")
        print("[X] - exit")
        print("-----------------------")

        choice = input("Enter you choice: ").lower()
        if choice == "x":
            print("Thank you!")
            input("Press any key to continue...")
            break
        elif choice == "a":
            print("\nADDITION")
            display_output("sum", addition)
        elif choice == "s":
            print("\nSUBTRACTION")
            display_output("difference", subtraction)
        elif choice == "m":
            print("\nMULTIPLICATION")
            display_output("product", multiplication)
        elif choice == "d":
            print("\nDIVISION")
            display_output("quotient", division)
        else:
            print("Choose only from the choices.")


# Problem 2
# Create a program compute the area of the following polygons and circle.
# - Area of square given the side.
# - Area of rectangle given the length and width.
# - Area of triangle given the base and height.
# - Area of circle given the radius

def compute_area():
    def area_of_square(side: float) -> float:
        return round(side * side, 2)

    def area_of_rectangle(length: float, width: float) -> float:
        return round(length * width, 2)
    
    def area_of_triangle(base: float, height: float) -> float:
        return round((base * height) / 2, 2)

    def area_of_circle(radius: float) -> float:
        return round(math.pi * (radius ** 2), 2)

    while True:
        print("\n***********************\nMENU\n***********************")
        print("[1] - Area of square") 
        print("[2] - Area of rectangle")
        print("[3] - Area of triangle")
        print("[4] - Area of circle")
        print("[5] - exit")
        print("-----------------------")

        choice = input("Enter your choice: ")
        print("-----------------------")

        if choice == "5":
            print("Thank you!")
            input("Press any key to continue...")
            break

        elif choice == "1":
            print("AREA OF SQUARE")
            print("-----------------------")
            try:
                side = float(input("Enter the side of the square: "))
                print(f"\nThe area is {area_of_square(side)} sq. units")
            except ValueError:
                print("Try again. The program only accepts numbers.")

        elif choice == "2":
            print("AREA OF RECTANGLE")
            print("-----------------------")
            try: 
                len_wid = input("Enter the length and the width of the rectangle: ").split(" ")
                print(f"\nThe area is {area_of_rectangle(float(len_wid[0]), float(len_wid[1]))} sq. units")
            except ValueError and IndexError:
                print("Try again. The program only accepts two numbers.")

        elif choice == "3":
            print("AREA OF TRIANGLE")
            print(line())
            try: 
                base_height = input("Enter the base and width of the triangle: ").split(" ")
                print(f"\nThe area is {area_of_triangle(float(base_height[0]), float(base_height[1]))} sq. units")
            except ValueError and IndexError:
                print("Try again. The program only accepts two numbers.")

        elif choice == "4":
            print("AREA OF CIRCLE")
            print(line())
            try:
                radius = float(input("Enter the radius: "))
                print(f"\nThe area is {area_of_circle(radius)} sq. units")
            except ValueError:
                print("Try again. The program only accepts numbers.")

        else: 
            print("Choose only from the choices.")


def main():
    print("Hello World!")
    basic_math_operations()
    compute_area()


if __name__ == "__main__":
    main()
