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

from ascii import logo

def calculator():
    print(logo)

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    continueCalc = True

    while continueCalc:
        operator = input("Choose an operation from the list above: ")
        num2 = float(input("What is the second number? "))
        calcFunction = operations[operator]
        answer = calcFunction(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation. ").lower() == "y":
            num1 = answer
        else:
            continueCalc = False
            calculator()

calculator()
