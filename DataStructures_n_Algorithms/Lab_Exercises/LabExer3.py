# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms
# Laboratory Exercise No. 3


def linechar():
    print("*" * 20)


def try_again():
    """
    Ask the user if they want to try again the program inside the while loop.
    """
    if input("\nTry again (y/n): ").lower() == "n":
        print(" ")
        return False
    else:
        print(" ")
        return True


def ask_two_words():
    """
    Ask the user two words.
    Returns a tuple containing the first word and the second word inputted.
    """
    first_word = input("Enter a first word (str1): ")
    second_word = input("Enter a second word (str2): ")
    return first_word, second_word


# Problem 1
# Convert the predefined function strcmp() to user defined function. 
# Note: strcmp() returns three values based on the lexicographical order of the characters based on the ASCII table


def strcmp(string1: str, string2: str) -> str:
    index = 0
    for k in string1:
        if k == string2[index]:
            index += 1
        else:
            if ord(k) - ord(string2[index]) < 0:
                return "negative"
            elif ord(k) - ord(string2[index]) > 0:
                return "positive"
    return "equal"


def display_strcmp():
    while True:
        linechar()
        print("STRING COMPARE")
        linechar()

        cmp_words = ask_two_words()
        print(strcmp(cmp_words[0], cmp_words[1]))

        if try_again() is False:
            break


# Problem 2
# Convert the predefined function strcpy() to user defined function. 

def strcpy(cpy_destination: str, cpy_source: str):
    cpy_destination = cpy_source
    return cpy_destination


def display_strcpy():
    while True:
        linechar()
        print("STRING COPY")
        linechar()
        
        cpy_first_word = input("Enter a first word (str1): ")
        cpy_second_word = input("Enter a second word (str2): ")

        cpy_first_word = strcpy(cpy_first_word, cpy_second_word)
        print("new string value for str1: " + cpy_first_word)

        if try_again() is False:
            break


# Problem 3
# Convert the predefined function strcat() to user defined function. 

def strcat(cat_destination: str, cat_source: str):
    """Return the concatenated strings."""
    return cat_destination + cat_source


def display_strcat():
    while True:
        linechar()
        print("STRING CONCATENATION")
        linechar()
        
        cat_words = ask_two_words()
        print("concatenated value: " + strcat(cat_words[0], cat_words[1]))

        if try_again() is False:
            break


# Problem 4
# Convert a program that will determine if the given word input is a palindrome. 
# The program will trim the trailing spaces of the given word.
# HINT: Create a user defined function for getting the length of the string and 
# a string trim function for eliminating trailing white spaces.


def elim_whitespace(string_w_whitespace):
    word_list = string_w_whitespace.split()

    string_wo_whitespace = ""
    for i in word_list:
        string_wo_whitespace += i + " "

    return string_wo_whitespace


def check_palindrome(check_string: str):
    word = check_string.lower()     # lower all characters (capitalized character(s) will be considered)
    word = word.replace(" ", "")    # remove spaces between characters

    # check the word if palindrome using slicing
    if word == word[::-1]:
        return True
    else:
        return False


def display_palindrome():
    while True:
        linechar()
        print("PALINDROME")
        linechar()

        check_word = input("Enter a word: ")
        string_wo_whtspc = elim_whitespace(check_word)

        if check_palindrome(check_word) is True:
            print(string_wo_whtspc + "is a palindrome")
        elif check_palindrome(check_word) is False:
            print(string_wo_whtspc + "is not a palindrome")
        
        if try_again() is False:
            break


# Problem 5
# Create a program that will capitalize each word from the string input.

def capitalize_first_letter(word_phrase: str):
    word_phrase_lower = word_phrase.lower()
    word_phrase_list = word_phrase_lower.split()

    for i in word_phrase_list:
        for j in i:
            j.replace(j[0], j.upper())

    word_phrase_join = " ".join(word_phrase)
    return word_phrase_join


def display_capitalize_first_letter():
    while True:
        strings_to_cap = input("Enter some string: ")

        print(capitalize_first_letter(strings_to_cap))

        if try_again() is False:
            break


def main():
    # display_strcmp()
    # display_strcpy()
    # display_strcat()
    # display_palindrome()
    display_capitalize_first_letter()


if __name__ == "__main__":
    main()
