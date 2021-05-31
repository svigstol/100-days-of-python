# 100 Days of Python
# Day 10.2 - Days In A Month
# Enter year and month as inputs. Then, display number of days in that month
# for that year.
# Sarah Vigstol
# 5/31/21

def isLeap(year):
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
    monthLength = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(year) == True:
        if month == 2:
            monthLength[1] = 29
        return monthLength[month - 1]
    else:
        return monthLength[month - 1]

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

for key in monthNames:
    if key == month:
        monthName = monthNames.get(key)

days = daysInMonth(year, month)
print(f"There were {days} days in {monthName} of {year}.")
