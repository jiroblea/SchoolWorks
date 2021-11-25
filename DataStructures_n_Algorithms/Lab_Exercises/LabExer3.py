# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms
# Laboratory Exercise No. 3


def linechar():
    print("*" * 20)


# Problem 1
# Convert the predefined function strcmp() to user defined function. 
# Note: strcmp() returns three values based on the lexicographical order of the characters based on the ASCII table


def strcmp(string1: str, string2: str) -> str:

    index = 0
    for k in string1:
        if k == string2[index]:
            index += 1
        else:
            if ord(k) - ord(string2[index]) < 0 :
                return "negative"
            elif ord(k) - ord(string2[index]) > 0 :
                return "positive"
    return "equal"


def display_strcmp():
    while True:
        linechar()
        print("STRING COMPARE")
        linechar()
        first_word = input("Enter a first word (str1): ")
        second_word = input("Enter a second word (str2): ")
        print(strcmp(first_word, second_word))

        if input("\nTry again (y/n): ").lower() == "n":
            print(" ")
            break
        else:
            print(" ")
        


def main():
    display_strcmp()


if __name__ == "__main__":
    main()
