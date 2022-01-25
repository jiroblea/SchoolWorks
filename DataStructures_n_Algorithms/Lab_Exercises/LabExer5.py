# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms
# Laboratory Exercise No. 5

from tabulate import tabulate

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


# Problem 1
# Create a program that will ask the user to enter the student record with three quizzes. The program will
# display the student record together with the average grade of the three quizzes and display a remark if
# the student passed the subject or not. The structure must compose of three members the id, the name,
# and the quiz in array form.

def student_record():
    """
    Program for problem 1.
    """

    def ask_student_record():
        """
        Asks the user to enter the student record with three quizzes. 
        """
        print("Enter Student Record")
        student_id = input("ID: ")
        student_name = input("Name: ")
        while True:
            try:
                student_quiz1 = float(input("Quiz 1: "))
                student_quiz2 = float(input("Quiz 2: "))
                student_quiz3 = float(input("Quiz 3: "))
                break
            except ValueError:
                print("Error: Please enter a grade only.")

        return student_id, student_name, student_quiz1, student_quiz2, student_quiz3


    def quiz_average_grade(student_quiz1, student_quiz2, student_quiz3):
        """
        Evaluates the quizzes' average.
        """
        average_grade = (student_quiz1 + student_quiz2 + student_quiz3) / 3
        return float("{:.4f}".format(average_grade))
                

    def display_student_record(student_id, student_name, average_grade):
        """
        Displays the student's record.
        """
        remarks = ""
        if average_grade >= 75:
            remarks = "Passed"
        else: 
            remarks = "Failed"

        print("\nStudent Record:")
        print(f"ID: {student_id}")
        print(f"Name: {student_name}")
        print(f"Grades: {average_grade}")
        print(f"Remarks: {remarks}")
        return None
        

    var_student_record = ask_student_record()
    var_average_grade = quiz_average_grade(var_student_record[2], var_student_record[3], var_student_record[4])
    display_student_record(var_student_record[0], var_student_record[1], var_average_grade)
    return None



# Problem 2
# Create a program that will enter 5 student records with three quizzes. The program will generate an
# output that will displays all the student records with their grades and remarks.
# grades = average grade of the three quizzes
# 75 is the passing mark.

def five_student_record():
    """
    Program for problem 2
    """

    def quiz_average_grade(student_quiz1, student_quiz2, student_quiz3):
        """
        Evaluates the average of 3 quizzes.
        """
        average_grade = (student_quiz1 + student_quiz2 + student_quiz3) / 3
        return float("{:.2f}".format(average_grade))

    
    def ask_5_student_record():
        """
        Asks the user to enter five student records with three quizzes. 
        """

        # lists of student record
        student_id_list = []
        student_name_list = []
        student_grade_list = []

        print("Enter 5 Student(s) Record")

        for i in range(1,6):
            print(f"\nStudent {i}")
            student_id = input("ID: ")
            student_name = input("Name: ")
            student_3_quizzes_float = []
            
            # asks and checks if the 3 quizzes scores are numbers
            while True:
                try:
                    student_3_quizzes_str = input("Enter 3 quiz(zes): ").split()
                    for i in student_3_quizzes_str:
                        student_3_quizzes_float.append(float(i))

                    student_grade = quiz_average_grade(student_3_quizzes_float[0], student_3_quizzes_float[1], student_3_quizzes_float[2])
                    break
                except ValueError:
                    print("Error: Please enter 3 grades only.")
                except IndexError:
                    print("Error: Please enter 3 grades only.")

            student_id_list.append(student_id)
            student_name_list.append(student_name)
            student_grade_list.append(student_grade)

        return student_id_list, student_name_list, student_grade_list


    def display_5_student_record(student_id_list, student_name_list, student_grade_list):
        
        student_remark_list = []
        for grade in student_grade_list:
            if grade >= 75:
                student_remark_list.append("Passed")
            else: 
                student_remark_list.append("Failed")

        record = {"No.": [1, 2, 3, 4, 5],
                "Student No": student_id_list,
                "Name": student_name_list, 
                "Grade": student_grade_list, 
                "Remark": student_remark_list}

        print(" ")
        print(tabulate(record, headers="keys", tablefmt="plain", stralign="right"))
        return None


    five_student_record = ask_5_student_record()
    display_5_student_record(five_student_record[0], five_student_record[1], five_student_record[2])
    return None



# Problem 3
# Create a program that will give an output as shown on figure A.The program will ask to input three
# customers information. Each customer have three items purchased. 

def customer_information():
    """
    Program for problem 3. 
    """
    # TODO: create a function to calculate total price and display the customer information

    def item_information(item_id: int):
        """
        Contain the items - ID as key and value are list of their name and price.
        Accepts an int argument as ID.
        Return a tuple containing the name and price.
        """
        items = {
            1: ["Apple", 13], 
            2: ["Orange", 15], 
            3: ["Banana", 7],
            4: ["Ponkan", 5],
            5: ["Guava", 20],
            6: ["Longan", 2],
            7: ["Pear", 8]
        }

        return items[item_id][0], items[item_id][1]


    def ask_customer_information():
        """
        Asks the user to enter 3 customer information.
        """
        # lists of customer information
        customer_name_list = []
        customer_contact_no_list = []
        customer_order_date_list = []
        customer_item_id_list = []
        customer_item_quantity_list = []

        print("Enter 3 customers")
        for i in range(1,4):
            print(f"\nCUSTOMER INFORMATION {i}")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            contact_no = input("Contact No: ")

            # for managing customer's name
            customer_name = f"{last_name}, {first_name}"
            
            # for managing the order date - checking if the date is valid
            print("Order Date: ")
            while True:
                try:
                    order_day = int(input("Day: "))
                    if order_day < 1 or order_day > 31:
                        raise IndexError
                    order_month = int(input("Month: "))
                    if order_month < 1 or order_month > 12:
                        raise IndexError
                    order_year = int(input("Year: "))
                    break
                except ValueError:
                    print("Error: Please enter an integer value only.")
                except IndexError:
                    print("Error: Please enter a valid date.")
            order_date = f"{order_month}/{order_day}/{order_year}"

            # for managing the 3 items
            item_id_list = []
            item_id_quantity = []

            print("Enter 3 items")
            for _ in range(3):
                while True: 
                    try: 
                        item_id = int(input("ID: "))
                        if item_id > 7:  # change the value depending on the number of items that can be bought
                            raise IndexError
                        item_desc = item_information(item_id)
                        print(f"Name: {item_desc[0]} \nPrice: {item_desc[1]}")
                        item_quantity = int(input("Quantity: "))
                        break
                    except ValueError:
                        print("Error: Please enter an integer value only.")
                    except IndexError:
                        print("Error: Please enter a valid value.")
                
                item_id_list.append(item_id)
                item_id_quantity.append(item_quantity)     

            customer_name_list.append(customer_name)
            customer_contact_no_list.append(contact_no)
            customer_order_date_list.append(order_date)
            customer_item_id_list.append(item_id_list)
            customer_item_quantity_list.append(item_id_quantity)

        return (customer_name_list, customer_contact_no_list, customer_order_date_list, 
                customer_item_id_list, customer_item_quantity_list)


    def display_customer_information(customer_name_list, customer_order_date_list, 
                                    customer_item_id_list, customer_item_quantity_list):
        """
        Display customer information.
        """

        item_name_list = []
        item_price_list = []
        for i in customer_item_id_list:
            for j in i:
                item_desc = item_information(j)
                item_name_list.append(item_desc[0])
                item_price_list.append(item_desc[1])

        # for lists of item quantity
        item_quantity_list = []
        for k in customer_item_quantity_list:
            for l in k:
                item_quantity_list.append(l)

        total_price = []
        for m in range(9):
            total_price.append(item_price_list[m] * item_quantity_list[m])


        record = {"#": [1, None, None, None, None, 
                        2, None, None, None, None, 
                        3],
                "Customer Name": [customer_name_list[0], None, None, None, None, 
                                customer_name_list[1], None, None, None, None, 
                                customer_name_list[2]],
                "Order Date": [customer_order_date_list[0], None, None, None, None, 
                                customer_order_date_list[1], None, None, None, None, 
                                customer_order_date_list[2]], 
                "Items": [None, item_name_list[0], item_name_list[1], item_name_list[2], "TOTAL PRICE: ",
                        None, item_name_list[3], item_name_list[4], item_name_list[5], "TOTAL PRICE: ",
                        None, item_name_list[6], item_name_list[7], item_name_list[8], "TOTAL PRICE: ",], 
                "Price": [None, float(item_price_list[0]), float(item_price_list[1]), float(item_price_list[2]), None,
                        None, float(item_price_list[3]), float(item_price_list[4]), float(item_price_list[5]), None, 
                        None, float(item_price_list[6]), float(item_price_list[7]), float(item_price_list[8]), None],
                "Quantity": [None, customer_item_quantity_list[0][0], customer_item_quantity_list[0][1], customer_item_quantity_list[0][2],
                            float(total_price[0] + total_price[1] + total_price[2]), 
                            None, customer_item_quantity_list[1][0], customer_item_quantity_list[1][1], customer_item_quantity_list[1][2],
                            float(total_price[3] + total_price[4] + total_price[5]),
                            None, customer_item_quantity_list[2][0], customer_item_quantity_list[2][1], customer_item_quantity_list[2][2],
                            float(total_price[6] + total_price[7] + total_price[8])]
        }

        print("\nSUMMARY REPORT")
        print(tabulate(record, headers="keys", tablefmt="plain", stralign="right", numalign="right"))
        return None

    customer_info = ask_customer_information()
    display_customer_information(customer_info[0], customer_info[2], customer_info[3], customer_info[4])
    return None



def main():
    # Problem 1
    while True:
        student_record()
        if try_again() is False:
            break

    # Problem 2
    five_student_record()

    # Problem 3
    customer_information()

if __name__ == "__main__":
    main()
