# 100 Days of Python
# Day 10.1 - Name Formatter
# Practice with function outputs
# Sarah Vigstol
# 5/31/21

def formatName(firstName, lastName):
    if firstName == "" or lastName == "":
        return "Invalid input."
    formattedFirstName = firstName.title()
    formattedLastName = lastName.title()
    return f"Result: {formattedFirstName} {formattedLastName}"

print(formatName(input("What is your first name? "), input("What is your last name? ")))
