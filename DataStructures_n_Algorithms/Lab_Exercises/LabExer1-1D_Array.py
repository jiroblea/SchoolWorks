# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms 
# Laboratory Exercise No. 1

# Problem 1 
# Create a program that will ask the user to enter 10 numbers and display it in ascending order.

def sort_ten_digits():
    """Ask for 10 digits and sort them in ascending order."""

    while True:
        digits = input("Enter 10 numbers:\n")   # ask the user for 10 digits
        digits_list = digits.split()            # put each digit to a list

        try:
            index = 0
            for i in digits_list:
                digits_list[index] = float(i)   # convert each digit from the digits_list to a float type
                index += 1
            break                               # end the while loop if no error occured
        except Exception as e:
            print(e)
            print("Some value entered were not a number.")

            # ask the user to try again or end the program if an error occured
            again = input("Try again (y/n)? ").lower()
            if again == "n":
                break
    
    try:
        # to end the program if digits can't be converted to float
        for i in digits_list:
            if type(i) != float:
                raise Exception

        digits_list2 = digits_list  # second list for selection sort

        # sort the 10 digits using selection sort
        sorted_list2 = []
        for j in range(len(digits_list2)):
            for i in digits_list2:
                if i == min(digits_list2):
                    sorted_list2.append(i)
                    digits_list2.remove(i)
        sorted_list = sorted_list2

        # sorting in ascending order using sorted() function in python
        # sorted_list = sorted(digits_list)

        index = 0
        for i in sorted_list:
            sorted_list[index] = str(i)   # convert each digit from the sorted_list to a string type
            index += 1

        space = " "
        print("Element value in ascending order:")
        print(space.join(sorted_list))
    except Exception:
        print("The program stopped...")

    return 


# Problem 2
# Create a program that will convert a decimal number (positive value) to its equivalent binary number. (Use array for binary values)

def binary_equivalent():
    """Outputs binary equivalent of inputted decimal number. \nNote: Only works at positive integer numbers."""
    
    while True:
        number = input("Enter a decimal number\t: ")

        try:
            number = float(number)  # convert the inputted string to a float type
            break                   # break the while loop if no error occured
        except Exception as e:
            print(e)

            # ask the user to try again or end the program if an error occured
            again = input("Try again (y/n)? ").lower()
            if again == "n":
                break

    try:
        binary = ""
        if number == 0:     # add string 0 if the number is exactly zero
            binary += "0"
        
        # calculate the binary by repeatedly dividing the number by two
        while number != 0:
            if (number % 2) == 1:       # If the number has a remainder,
                binary += "1"           # add string 1 to the string variable binary.
                number = int(number / 2)    # changes the value of number for the next loop
            elif (number % 2) == 0:     # If the number has no remainder,
                binary += "0"           # add string 0 to the string variable binary. 
                number = int(number / 2)    # changes the value of number for the next loop
        
        answer = binary[::-1]           # reverse the string variable binary to get the proper answer
        print(f"Binary equivalent\t: {answer}")
    except Exception:
        print("The program stopped...")
    
    return 


# Problem 3
# Create a program that will ask the user to enter 10 numbers and display the 1st and 2nd to 
# highest number and 1st and 2nd to the lowest number. (Don't use array sorting)

def two_from_both_ends():
    """Display the first and the second highest and lowest numbers, respectively."""
    
    while True:
        digits = input("Enter ten (10) numbers:\n")   # ask the user for 10 digits
        digits_list = digits.split()            # put each digit to a list

        try:
            index = 0
            for i in digits_list:
                digits_list[index] = float(i)   # convert each digit from the list to a float type
                index += 1
            break                               # end the while loop if no error occured
        except Exception as e:
            print(e)
            print("Some value entered were not a number.")

            # ask the user to try again or end the program if an error occured
            again = input("Try again (y/n)? ").lower()
            if again == "n":
                break

    try:
        # find the highest two numbers
        highest1 = 0
        highest2 = 0
        for i in digits_list:
            if i > highest1:
                highest2, highest1 = highest1, i    # highest2 = highest1, highest1 = i
            elif i > highest2:                      # if i is lower than highest but higher than second highest
                highest2 = i

        # finding the lowest two numbers
        lowest1 = highest1
        lowest2 = highest1
        for i in digits_list:
            if i < lowest1:
                lowest2, lowest1 = lowest1, i       # lowest2 = lowest1, lowest1 = i
            elif i < lowest2:                       # if i is higher than lowest but lower than the second lowest
                lowest2 = i
        
        print(f"\nfirst to the highest\t: {highest1}")
        print(f"second to the highest\t: {highest2}")
        print(f"first to the lowest\t: {lowest1}")
        print(f"second to the lowest\t: {lowest2}")
    except Exception:
        print("The program stopped...")

    return


# Problem 4
# Create a program that will check if a given word is a palindrome or not a palindrome.

def check_if_palindrome():
    """Check if the entered word is a palindrome or not."""

    raw_word = input("Enter a word: ")
    word = raw_word.lower()             # lower all characters (capitalized character(s) will be considered)
    # word = word.replace(" ", "")        # remove spaces between characters for it not to be considered

    # check the word if palindrome using indexing
    mirrored_characters = 0
    for i in range(len(word)):
        if word[i] == word[-(i+1)]:     # check the ith character of the word if it is the same with its ith character counting from the last letter
            mirrored_characters += 1    # count the number of correct mirrored characters
    
    if mirrored_characters == len(word):
        print(f"{raw_word} is a palindrome")
    else:
        print(f"{raw_word} is not a palindrome")

    # check the word if palindrome using slicing
    # if word == word[::-1]:
    #     print(f"{raw_word} is a palindrome")
    # elif word != word[::-1]:
    #     print(f"{raw_word} is not a palindrome")
    
    return


def main():
    print("Laboratory Exercise 1")

    print("\nProblem 1 \nA program that will ask the user to enter 10 numbers and display it in ascending order.")
    sort_ten_digits()     # problem 1
    input("\nPress anything to continue... ")

    print("\nProblem 2 \nA program that will convert a decimal number (positive value) to its equivalent binary number.")
    binary_equivalent()   # problem 2
    input("\nPress anything to continue... ")

    print("\nProblem 3 \nA program that will ask the user to enter 10 numbers and display the 1st and 2nd to highest number and 1st and 2nd to the lowest number.")
    two_from_both_ends()  # problem 3
    input("\nPress anything to continue... ")

    print("\nProblem 4 \nA program that will check if a given word is a palindrome or not a palindrome.")
    check_if_palindrome() # problem 4

main()
