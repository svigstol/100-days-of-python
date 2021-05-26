# 100 Days of Python
# Day 9.1 - Grading Program
# Sarah Vigstol
# 5/25/21

studentScores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

studentGrades = {}

# loop through values
for score in studentScores:
	# compare scores
	if studentScores[score] >= 91:
	# assign grades
		print("Outstanding")
	elif studentScores[score] >= 81 and studentScores[score] <= 90:
		print("Exceeds Expectations")
	elif studentScores[score] >= 71 and studentScores[score] <= 80:
		print("Acceptable")
	elif studentScores[score] <= 70:
		print("Fail")

print(studentGrades)
