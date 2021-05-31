# 100 Days of Python
# Day 10 - Calculator Program
# Enter two numbers and an operation, then display output.
# Allow user to perform additional calculators using the result
# Sarah Vigstol
# 5/31/21

def add(n1, n2):
    """Add two numbers together and return the sum"""
    return n1 + n2

def subtract(n1, n2):
    """Subtract a number from another and return the difference"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply a number by another number and return the product"""
    return n1 * n2

def divide(n1, n2):
    """Divide a number by another number and return the quotient"""
    return n1 / n2

calcFinish = False

while not calcFinish:
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))

    for symbol in operations:
        print(symbol)

    operator = input("Choose an operation from the list above: ")
    calcFunction = operations[operator]
    answer = calcFunction(num1, num2)

    print(f"{num1} {operator} {num2} = {answer}")

    goAgain = input("Calculate again? Type 'yes' or 'no.' ")
    if goAgain == "yes":
        print("Loading...")
    elif goAgain == "no":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Try again.")
