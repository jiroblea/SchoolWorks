# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms 
# Laboratory Exercise No. 2

from math import e, pi

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

def try_again():
    """
    Located in while True loop.
    Asks the user if they want to try again the program inside the while loop.
    """
    again = input("\nTry again (y/n)? ").lower()
    if again == "n":
        print("Thank you!")
        input("Press any key to continue...")
        return False


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
        
        if try_again() == False:
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
                print(f"The {result_name} is:", round(know_num_type(fnctn(*num)), 2))   # uses splat operator to call elements in num
        except:
            print("Try again.")

    while True:
        print("\nARITHMETIC CALCULATOR")
        print(line())
        print("[1] - Addition") 
        print("[2] - Subtraction")
        print("[3] - Multiplication")
        print("[4] - Division")
        print(line())

        choice = input("Enter you choice: ").lower()
        if choice == "1":
            display_output("sum", addition)
        elif choice == "2":
            display_output("difference", subtraction)
        elif choice == "3":
            display_output("product", multiplication)
        elif choice == "4":
            display_output("quotient", division)
        else:
            print("Choose only from the choices.")

        if try_again() == False:
            break


# Problem 5
# Create a program that will overload a function named linechar that display a line of characters.

def linechar(char = "*", amount = 20):
    print(char * amount)


# Problem 6
# Create a program that will ask the user to enter ten numbers and get the sum of all odd numbers. 
# - The numbers will be stored in array
# - The array value will be pass as argument to the function

def sum_odd_numbers():

    # function that get the sum of odd numbers
    def sum_of_odds(num_list: list):
        result = 0
        for i in num_list:
            if i % 2 == 0:
                continue
            elif (i + 1) % 2 == 0: 
                result += i
        
        return result

    while True:
        numbers = input("\nEnter 10 numbers: ").split(" ")    # asks user for 10 numbers

        # numbers will be stored in an array
        numbers_int = []
        for i in numbers:
            try:
                numbers_int.append(int(i))
            except ValueError as e:
                print(f"error: {e}")

        print("The sum of all odd numbers is", sum_of_odds(numbers_int))

        if try_again() == False:
            break

# Problem 7
# Create a program that will add two numbers, three numbers and four numbers. Use function overloading named add. 
# - Use two arguments for adding two numbers
# - Use three arguments for adding three numbers
# - Use array with size 4 for adding four numbers
# - The function add will return the value of the sum of the numbers

def add(num1 = 0, num2 = 0, num3 = 0, num4 = 0):
    try:
        return num1 + num2 + num3 + num4
    except ValueError as e:
        print("error:", e)

def get_and_display_add():
    """
    To get the input of users and display the results of add() function.
    """
    def convert_to_float(string_list: list):
        num_list = []
        for i in string_list:
            try:
                num_list.append(float(i))
            except ValueError:
                print(f"{i} is not a number.")
        return num_list

    while True:
        try:
            two_num = input("Enter two numbers: ").split(" ")
            two_list = convert_to_float(two_num)
            print("The sum is:", know_num_type(add(*two_list)))
        except Exception as e:
            print(e)

        try:
            three_num  = input("Enter three numbers: ").split(" ")
            three_list = convert_to_float(three_num)
            print("The sum is:", know_num_type(add(*three_list)))
        except Exception as e:
            print(e)

        try:
            four_num = input("Enter four numbers: ").split(" ")
            four_list = convert_to_float(four_num)
            print("The sum is:", know_num_type(add(*four_list)))
        except Exception as e:
            print(e)

        if try_again() == False:
            break


# Problem 8
# Create a program that will overload a function named substring. The function will ask the user to 
# enter the index range of the substring inclusive. Using the function defined, the program will display the 
# whole string value, the substring given the start index, and the substring given the start and last index.

def substring(string: str, start = 0, end = None):
    print(string[start:end])

def get_substring_value():
    while True:
        substring_list = input("\nOriginal string value:\n")
        print(f"String length: {len(substring_list)}")
        
        try: 
            start_index = int(input("\nEnter start index: "))
            end_index = int(input("Enter end index: "))

            print("\nfunction substring(str):")
            substring(substring_list)

            print(f"\nfunction substring(str, {start_index}):")
            substring(substring_list, start_index)

            print(f"\nfunction substring(str, {start_index}, {end_index}):")
            if start_index > end_index or  start_index < 0:
                raise Exception
            substring(substring_list, start_index, end_index + 1)

        except ValueError:
            print("The program only accepts integers.")
        except Exception:
            print("Error: The value of start index is either greater than end index or lower than zero.")

        if try_again() == False:
            break


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
    print("\nProblem 6")
    sum_odd_numbers()
    print("\nProblem 7\n")
    get_and_display_add()
    print("\nProblem 8")
    get_substring_value()


if __name__ == "__main__":
    main()
