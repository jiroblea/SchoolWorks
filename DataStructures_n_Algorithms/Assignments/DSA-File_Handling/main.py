# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms
# File Handling in Python

import os

# Problem 1
# Create a python program that will search string/strings (can use operator such as s* - all that starts with s,
# *sdf* etc..) in a txt file and returns something such as # of times the string/strings appears


def search_string(file_path: str, list_of_string: str):
    # read each line of text file
    with open(file_path, "r") as file:
        # txt_file_lines = file.readlines()   # a list of lines from text file

        txt_file_word_list = []
        for i in file.readlines():
            txt_file_word_list.append(i.split(" "))

    # create a list of words in each line
    # txt_file_word_list = []     # a 2D array containing a list of words inside a list of lines of words
    # for i in txt_file_lines:
    #     txt_file_word_list.append(i.split(" "))

    searched_words = []
    for j in txt_file_word_list:    # scan the lines
        for k in j:                 # scan the words in each line
            if list_of_string in k:
                searched_words.append(k)

    without_slash = []
    for el in searched_words:
        if "\n" in el:
            without_slash.append(el[0:-1])
        else:
            without_slash.append(el)
    print(without_slash)

    string_at_front = []
    string_at_back = []
    string_at_mid = []
    for elem in without_slash:
        if list_of_string in elem[0:len(list_of_string)]:
            string_at_front.append(elem)
        elif list_of_string in elem[1:-1]:
            string_at_mid.append(elem)
        elif list_of_string in elem[-len(list_of_string):None]:
            string_at_back.append(elem)

    return len(searched_words), len(string_at_front), len(string_at_mid), len(string_at_back), string_at_front, \
           string_at_mid, string_at_back


def display_searched_string():
    while True:
        try:
            file_name = input("Insert the path of the text file: ")
            list_of_string = input("Enter the string you want to find: ")

            placement = 0
            strings = ""
            if "*" in list_of_string:
                if "*" in (list_of_string[0] and list_of_string[-1]):   # list of string in the middle
                    placement = 2
                    strings = list_of_string[1:-1]
                elif "*" in list_of_string[0]:    # list of string at the back
                    placement = 3
                    strings = list_of_string[1:]
                elif "*" in list_of_string[-1]:     # list of string in front
                    placement = 1
                    strings = list_of_string[0:-1]

            print(f"Number of time(s) the string appears: {search_string(file_name, strings)[placement]}")
            if input("\nTry again (y/n)? ") == "n":
                break

        except FileNotFoundError and OSError:
            print("\nFile not found")
            if input("Try again (y/n)? ") == "n":
                break


# Problem 2
# A python program that will search file from a directory or entire drive

def search_file(directory_path: str):
    for (dirpath, dirnames, filenames) in os.walk(directory_path, topdown=True):
        # print(dirpath)
        # print(dirnames)
        # print(filenames)
        # print('--------------------------------')
        for i in filenames:
            if i == "Anime.txt":
                return dirpath


def main():
    print("Hello World!")
    display_searched_string()
    print(search_file("C:/Users/jiroo"))


if __name__ == '__main__':
    main()
