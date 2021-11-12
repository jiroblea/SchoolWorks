# Student: Junius Iosif R. Oblea
# Program: BS Computer Engineering 2-1
# Subject: CMPE 30052 Data Structures and Algorithms 
# Stacks


# Section 1
def stack_demonstration():
    """
    append() - insertion in LIFO
    pop() - deletion in LIFO
    """

    stack = ["A", "C", "D", "F", "K"]
    print("Initial Stack: ")
    print(stack)

    def condition(stack):
        if len(stack) < 8:
            print("Elements in Stack: ")
            print(stack)
        elif len(stack) == 0:
            print("Stack is empty")
        elif len(stack) > 8:
            print("Stack is over eight elements: ")
            print(stack)

    stack.pop()
    condition(stack)
    stack.pop()
    condition(stack)
    stack.append("L")
    condition(stack)
    stack.append("P")
    condition(stack)
    stack.pop()
    condition(stack)
    stack.append("R")
    condition(stack)
    stack.append("S")
    condition(stack)
    stack.pop()
    condition(stack)


def main():
    print("Hello World!")
    stack_demonstration()

if __name__ == "__main__":
    main()
