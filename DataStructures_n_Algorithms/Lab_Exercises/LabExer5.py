# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering
# Subject: CMPE 30052 Data Structures and Algorithms
# Laboratory Exercise No. 5


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
                print("Only accepts numbers.")

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
    

    var_student_record = ask_student_record()
    var_average_grade = quiz_average_grade(var_student_record[2], var_student_record[3], var_student_record[4])
    display_student_record(var_student_record[0], var_student_record[1], var_average_grade)



# Problem 2
# Create a program that will enter 5 student records with three quizzes. The program will generate an
# output that will displays all the student records with their grades and remarks.
# grades = average grade of the three quizzes
# 75 is the passing mark.


# Problem 3
# Create a program that will give an output as shown on figure A.The program will ask to input three
# customers information. Each customer have three items purchased. 


def main():
    # Problem 1
    while True:
        student_record()
        if try_again() is False:
            break

if __name__ == "__main__":
    main()
