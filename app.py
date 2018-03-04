import os
import re

  # ex.1
# We have variable a and variable b. Both variables have already a stored value. We want to swap those values.

# * Example: a = 10, b = 20
# * Output: a = 20, b = 10
# 

a = 10
b = 20
a = 20
b = 10
print('a: ' + str(a))
print('b: ' + str(b))

# Warning! Do not use the programming language magic. After you complete the exercise feel free to do so.

# ex.2
# It's the end of the semester and you got your marks from, Geometry, Algebra, Physics classes.

# Create a program that:
# * Reads the values of these 3 lessons
# * Calculates the average of your grades
# * Example: Geometry = 6, Algebra = 7, Physics = 8
# * Output: average_score = 7

# Warning! Do not use the programming language magic. After you complete the exercise feel free to do so.
# 
grades = {'geometry': 6, 'algegra': 7, 'physics': 8}
print(grades) #geometry', 'physics', 'algegra'}
print(grades['geometry']) #6

print(list(grades)) #['geometry', 'physics', 'algegra']
print(grades.keys())#['geometry', 'physics', 'algegra']
print(grades.values())#[6, 8, 7]
print(sum(grades.values()) / len(grades))#7
average_score = sum(grades.values()) / len(grades)
print(average_score) #7






