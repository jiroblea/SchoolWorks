# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms 
# Laboratory Exercise No. 1

# Problem 1
# Create a program that will add, subtract, multiply and divide two numbers.
# - Use user defined function for each operator
# - Any number divided by zero will result to undefined
# - Use int data type only for all variables declared


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
            return num1 // num2
        except ZeroDivisionError:
            return "undefined!"

    def ask_number_input() -> tuple:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("The program only accept integers.")

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
            try:
                num = ask_number_input()
                print("The sum is", addition(num[0], num[1]))
            except:
                print("Try again.")

        elif choice == "s":
            print("\nSUBTRACTION")
            try:
                num = ask_number_input()
                print("The difference is", subtraction(num[0], num[1]))
            except:
                print("Try again.")

        elif choice == "m":
            print("\nMULTIPLICATION")
            try:
                num = ask_number_input()
                print("The product is", multiplication(num[0], num[1]))
            except:
                print("Try again.")
                
        elif choice == "d":
            print("\nDIVISION")
            try:
                num = ask_number_input()
                print("The quotient is", division(num[0], num[1]))
            except:
                print("Try again.")
        else:
            print("Choose only from the choices.")


def main():
    print("Hello World!")
    basic_math_operation()


if __name__ == "__main__":
    main()
