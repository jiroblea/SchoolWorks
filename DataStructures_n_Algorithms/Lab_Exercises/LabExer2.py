# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms 
# Laboratory Exercise No. 2

from math import pi

def line():
    return "-----------------------"


def know_num_type(number: float) -> (int | float):
    """
    Return the proper type of argument passed if it is really float or int.
    """
    if number % 1 == 0:
        return int(number)
    else:
        return float(number)


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
            return num1 / num2
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
                print(f"The {result_name} is", round(know_num_type(fnctn(num[0], num[1])), 2))
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
        return round(pi * (radius ** 2), 2)

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
            print(line())
            try:
                side = float(input("Enter the side of the square: "))
                print(f"\nThe area is {area_of_square(side)} sq. units")
            except ValueError:
                print("Try again. The program only accepts a number.")

        elif choice == "2":
            print("AREA OF RECTANGLE")
            print(line())
            try: 
                len_wid = input("Enter the length and the width of the rectangle: ").split(" ")
                if len(len_wid) != 2:
                    raise IndexError
                print(f"\nThe area is {area_of_rectangle(float(len_wid[0]), float(len_wid[1]))} sq. units")
            except ValueError and IndexError:
                print("Try again. The program only accepts two numbers.")

        elif choice == "3":
            print("AREA OF TRIANGLE")
            print(line())
            try: 
                base_height = input("Enter the base and height of the triangle: ").split(" ")
                if len(base_height) != 2:
                    raise IndexError
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
                print("Try again. The program only accepts a number.")

        else: 
            print("Choose only from the choices.")


# Problem 3
# Create a program that will compute the factorial of a given number.
# - Use function to pass the value of the number input and ...
# ... to pass the reference of the factorial value of the number

def compute_factorial():
    def find_factorial(number: int) -> int:
        factorial = number
        while number > 1:
            factorial *= (number - 1)
            number -= 1

        return factorial

    while True:
        try:
            num = int(input("\nEnter a number: "))
            print(f"The factorial of {num} is {find_factorial(num)}")
        except Exception:
            print("Only accepts an integer.")
        
        again = input("\nTry again (y/n)? ").lower()
        if again == "n":
            print("Thank you!")
            print("Press any key to continue...")
            break


# Problem 4
# Create a simple arithmetic calculator that will add, subtract, multiply and divide two integer numbers.
# - Use function to accept inputs for the two operands.

def arithmetic_calculator():
    def addition(num1: float, num2: float) -> float:
        return num1 + num2

    def subtraction(num1: float, num2: float) -> float:
        return num1 - num2

    def multiplication(num1: float, num2: float) -> float:
        return num1 * num2

    def division(num1: float, num2: float): 
        try:
            return round(num1 / num2, 2)
        except ZeroDivisionError:
            return "undefined!"

    def ask_number_input() -> tuple:
        """Function that accepts input for two operands."""
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("The program only accept numbers.")

    def display_output(result_name: str, fnctn):
        try:
            num = ask_number_input()
            if fnctn == division and num[1] == 0:
                print("Undefined!")
            else:
                print(f"The {result_name} is:", round(know_num_type(fnctn(num[0], num[1])), 2))
        except:
            print("Try again.")

    while True:
        print("\nPress 'x' to exit")
        print("\nARITHMETIC CALCULATOR")
        print(line())
        print("[1] - Addition") 
        print("[2] - Subtraction")
        print("[3] - Multiplication")
        print("[4] - Division")
        print(line())

        choice = input("Enter you choice: ").lower()
        if choice == "x":
            print("Thank you!")
            input("Press any key to continue...")
            break
        elif choice == "1":
            display_output("sum", addition)
        elif choice == "2":
            display_output("difference", subtraction)
        elif choice == "3":
            display_output("product", multiplication)
        elif choice == "4":
            display_output("quotient", division)
        else:
            print("Choose only from the choices.")


# Problem 5
# Create a program that will overload a function named linechar that display a line of characters.

def linechar(char = "*", amount = 20):
    print(char * amount)


def main():
    print("Problem 1")
    basic_math_operations()
    print("\nProblem 2")
    compute_area()
    print("\nProblem 3")
    compute_factorial()
    print("\nProblem 4")
    arithmetic_calculator()
    print("\nProblem 5\n")
    linechar()
    linechar("@")
    linechar(amount = 10)
    linechar("#", 15)


if __name__ == "__main__":
    main()
