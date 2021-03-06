# 100 Days of Python
# Day 10.2 - Days In A Month
# Enter year and month as inputs. Then, display number of days in that month
# for that year.
# Sarah Vigstol
# 5/31/21

def isLeap(year):
    """Determine whether or not a given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInMonth(year, month):
    """Check if the given year is a leap year, then returns the
    number of days in the given month."""
    monthLength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(year) == True and month == 2:
        return 29
    return monthLength[month - 1]

while True:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))
    monthNames = {
        1:"January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "Novemeber",
        12: "December"
        }

    if month <= 12 and month >= 1:
        for key in monthNames:
            if key == month:
                monthName = monthNames.get(key)
                days = daysInMonth(year, month)
                print(f"\nThere were {days} days in {monthName} of {year}.")
        break

    elif month > 12 or month < 1:
        print("Invalid month. Try again.\n")
