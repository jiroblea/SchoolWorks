# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms
# Laboratory Exercise No. 4

# Problem 1
# Create a programmer defined function that will do the same as strcpy function.

def strcpy(destination_cpy: str, source_cpy: str) -> str:
    destination_cpy = source_cpy
    return destination_cpy
	

# Problem 2
# Create a programmer defined function that will do the same as strcmp function.

def strcmp(string1: str, string2: str) -> int:
    index = 0
    for i in string1:
        if i == string2[index]:
            index += 1
        else:
            ascii_value_difference = ord(i) - ord(string2[index])
            if  ascii_value_difference < 0:
                return ascii_value_difference
            elif ascii_value_difference > 0:
                return ascii_value_difference
    return 0
    

# Problem 3
# Create a programmer defined function that will do the same as strcat function.

def strcat(destination_cat: str, source_cat: str) -> str:
    return destination_cat + source_cat


# Problem 4
# Create a programmer defined function that will do the same as strlen function.


# Problem 5
# Create a program that will return a reverse string using pointer.


def main():
    yo1 = "hello"
    yo2 = "wazzup"
    yo1 = strcpy(yo1, yo2)
	
    print(f"yo1: {yo1}\nyo2: {yo2}")  # dapat pag ginamit ang yo1 ay yo2 na
	
    print(strcmp(yo1, yo2))
    print(strcmp("hello", "Hello"))
    print(strcmp("Hello", "hello"))

    print(strcat(yo1, yo2))
	
main()
