# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms
# File Handling in Python

import os

# Problem 1
# Create a python program that will search string/strings (can use operator such as s* - all that starts with s,
# *sdf* etc..) in a txt file and returns something such as # of times the string/strings appears


def search_string(txt_file: str, string_to_find: str, placement_of_str: int):
    # read each line of text file
    with open(txt_file, "r", encoding="utf8") as file:
        txt_file_word_list = []     # a 2D array containing a list of words inside a list of lines of words
        for line in file:
            txt_file_word_list.append(line.split(" "))

    words_with_str_to_find = []
    for lines in txt_file_word_list:    # scan the lines
        for words in lines:             # scan the words in each line
            if string_to_find in words:
                words_with_str_to_find.append(words)

    # remove the "\n" from the end of the words
    without_slash = []
    for word_char in words_with_str_to_find:
        if "\n" in word_char:
            without_slash.append(word_char[0:-1])
        else:
            without_slash.append(word_char)

    string_at_front = []
    string_at_back = []
    string_at_mid = []
    if placement_of_str == 0:
        return len(without_slash), without_slash

    elif placement_of_str == 1:
        for elem in without_slash:
            if string_to_find in elem[:len(string_to_find)]:
                string_at_front.append(elem)
        return len(string_at_front), string_at_front

    elif placement_of_str == 2:
        for elem in without_slash:
            if string_to_find in elem[1:-1]:
                string_at_mid.append(elem)
        return len(string_at_mid), string_at_mid

    elif placement_of_str == 3:
        for elem in without_slash:
            if string_to_find in elem[-len(string_to_find):]:
                string_at_back.append(elem)
        return len(string_at_back), string_at_back


def display_searched_string():
    while True:
        try:
            file_name = input("\nEnter the file name of the txt file: ")
            str_to_find_w_asterisk = input("Enter the string to find: ")

            placement = 0
            str_to_find_wo_astrsk = str_to_find_w_asterisk
            if "*" in str_to_find_w_asterisk:
                if "*" == str_to_find_w_asterisk[0]:    # str_to_find is at the back
                    if "*" == str_to_find_w_asterisk[-1]:  # str_to_find is in the middle
                        placement = 2
                        str_to_find_wo_astrsk = str_to_find_w_asterisk[1:-1]
                    else:
                        placement = 3
                        str_to_find_wo_astrsk = str_to_find_w_asterisk[1:]
                elif "*" == str_to_find_w_asterisk[-1]:     # str_to_find is in front
                    placement = 1
                    str_to_find_wo_astrsk = str_to_find_w_asterisk[:-1]

            num_of_occurrence = search_string(file_name, str_to_find_wo_astrsk, placement)
            print(f"Number of times the string(s) appears: {num_of_occurrence[0]}")
            if input("Do you want to see those occurrences (y/n)? ").lower() == "y":
                print(num_of_occurrence[1])
            else:
                print(" ")

            if input("\nTry again (y/n)? ").lower() == "n":
                break

        except FileNotFoundError or OSError:
            print("\nFile not found")
            if input("Try again (y/n)? ").lower() == "n":
                break


# Problem 2
# A python program that will search file from a directory or entire drive

def search_file(dir_to_search: str, file_to_search: str):
    for (dirpath, dirnames, filenames) in os.walk(dir_to_search, topdown=True):
        for i in filenames:
            if i == file_to_search:
                return dirpath
    return False


def display_search_file():
    while True:
        try:
            be_search_upon = input("\nEnter a path directory or drive to be search upon (e.g.: C:/): ")
            file_name_to_find = input("Enter the file name to find: ")

            file_name_path = search_file(be_search_upon, file_name_to_find)
            if file_name_path is False:
                print(f"The program is unable to find the file '{file_name_to_find}' on '{be_search_upon}'")
                raise FileNotFoundError
            else:
                print(f"The file '{file_name_to_find}' is located in this path: {file_name_path}")

            if input("\nTry again (y/n)? ").lower() == "n":
                break

        except FileNotFoundError or OSError:
            print("\nPath or file not found")
            if input("Try again (y/n)? ").lower() == "n":
                break


def main():
    display_searched_string()
    display_search_file()


if __name__ == '__main__':
    main()
