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

# ex.3
# You've bought a Bitcoin and now it's on the rise!!!

# Create a program that:
# * Reads the value that you bought the bitcoin
# * Reads the percentage of increase(or decrease)
# * Prints the total value of your bitcoin
# * Prints the increase or decrease value
# * Example: bitcoin_value = 10000, bitcoin_increase = 10
# * Output: total_bitcoin_value = 11000, bitcoin_increase_value = 1000

bitcoin_value = 10000 
bitcoin_increase = float(1.10)
print('bitcoin value: ' + str(bitcoin_value))
print('bitcoint increase %: ' + str(bitcoin_increase))

total_value = bitcoin_value * bitcoin_increase
print('total value: ' + str(total_value))

bitcoin_increase_value = total_value - bitcoin_value;
print('bitcoin incease value: ' + str(bitcoin_increase_value))

percent_change = ((float(total_value) - bitcoin_value) / abs(bitcoin_value)) * 100.00
print('percent change: ' + str(percent_change))









