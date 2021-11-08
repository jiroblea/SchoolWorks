# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms 
# Laboratory Exercise No. 1

# Problem 1
# Create a program that will add, subtract, multiply and divide two numbers.
# - Use user defined function for each operator
# - Any number divided by zero will result to undefined
# - Use int data type only for all variables declared

from typing import SupportsBytes


def basic_math_operation():
    def addition(num1: int, num2: int) -> int:
        return num1 + num2

    def subtraction(num1: int, num2: int) -> int:
        return num1 - num2

    def multiplication(num1: int, num2: int) -> int:
        return num1 * num2

    def division(num1: int, num2: int): 
        """TODO: should not return float if possible"""
        try:
            if type(num1 / num2) == int: 
                return int(num1 / num2)
            else:
                raise ValueError
        except ZeroDivisionError:
            return "undefined!"
        except ValueError:
            return "{:.2f}".format(float(num1 / num2))


    def ask_number_input() -> tuple:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        return num1, num2

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
            num = ask_number_input()
            print("The sum is", addition(num[0], num[1]))
        elif choice == "s":
            print("\nSUBTRACTION")
            num = ask_number_input()
            print("The difference is", subtraction(num[0], num[1]))
        elif choice == "m":
            print("\nMULTIPLICATION")
            num = ask_number_input()
            print("The product is", multiplication(num[0], num[1]))
        elif choice == "d":
            print("\nDIVISION")
            num = ask_number_input()
            print("The quotient is", division(num[0], num[1]))
        else:
            print("I don't know that. Teach me more.")


def main():
    print("Hello World!")
    basic_math_operation()


if __name__ == "__main__":
    main()
