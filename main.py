# def greet():
#   print('Hello')
#   print('How are you?')

# greet()
# _______________________

# def greet(name):
#   print('Hello', name)
#   print('How are you?')

# greet('Jack')
# __________________________

# number1 = 5.4
# number2 = 6.7

# def addNum(n1, n2):
#   result = n1 + n2
#   print('The sum is', result)

# addNum(number1, number2)
# ________________________

# def addNum(n1, n2):
#   result = n1 + n2
#   return result

# result = addNum(number1, number2)
# print('The sum is', result)
# ________________________________

# marks = [55,64,75,80,34]
# finds length
# length = len(marks)
# print('Length is', length)

# finds sum of all numbers
# marksSum = sum(marks)
# print('The total marks you got is', marksSum)
# All built in function available in Python can be found in the programiz.com website.

# function to find average marks
# marks = [55,64,75,80,65]

# def findAverageMarks(marks):
#   sumOfMarks = sum(marks)
#   totalSubjects = len(marks)
#   averageMarks = sumOfMarks / totalSubjects
#   return averageMarks

# averageMarks = findAverageMarks(marks)
# print('Your average marks is', averageMarks)

# # calculate the grade and return it
# def computeGrade(averageMarks):
#   if averageMarks >= 80:
#     grade = 'A'
#   elif averageMarks >= 60:
#     grade = 'B'
#   elif averageMarks >= 50:
#     grade = 'C'
#   else:
#     grade = 'F'
#   return grade

# grade = computeGrade(averageMarks)
# print('Your grade is', grade)
# _____________________________

number1 = 5
number2 = 6

def addNumbers(num1, num2):
  result = num1 + num2
  return result

add = addNumbers(number1, number2)
print('The numbers added =', add)

def multiplyNumbers(num1, num2):
  result = num1 * num2
  return result

multiply = multiplyNumbers(number1, number2)
print('The numbers multiplied =', multiply)