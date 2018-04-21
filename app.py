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

# ex.4
# You own a property and you want to calculate the area.

# Create a program that:
# * Reads the width and height
# * Prints the area
# * Example: width = 5, height = 2
# * Output: area = 10

width = 5
height = 2
print('width: ' + str(width))
print('height: '+ str(height))
area = width * height
print('area: ' + str(area))

# ex.5
# You are interested in buying cryptocurrencies. You want to check with your current amount of money how many coins you can buy
# in Bitcoin, Ethereum and Litecoin.

# Create a program that:
# * Reads your amount of money
# * Reads the read the price of Bitcoin, Ethereum and Litecoin
# * Prints the amount of Bitcoin, Ethereum and Litecoin you can buy
# * Example: money = 100, bitcoin_price = 50, Ethereum = 25, Litecoin = 10
# * Output: "With 100$ you can buy 2 Bitcoin, 4 Ethereum, 10 Litecoin


money = 100
print(money)
bitcoin_price = 50
Ethereum = 25
Litecoin = 10

bitcoin_amount = money / bitcoin_price
print(bitcoin_amount)

Ethereum_amount = money / Ethereum
print(Ethereum_amount)

Litecoin_amount = money / Litecoin
print(Litecoin_amount)

print('With 100$ you can buy ' + str(bitcoin_amount) + ' Bitcoin, ' + str(Ethereum_amount) + ' Ethereum, ' + str(Litecoin_amount) + ' Litcoin.') 


# ex.6
# You are interested in buying a new laptop. You check the price and you see that the price is 300$ without 10% tax.

# Create a program that:
# * Read the price of the laptop
# * Read the tax percentage
# * Prints the total amount
# * Output: "The total price of the laptop is 330$"

laptop = 300
tax = 1.10
total_amount = laptop * tax
print('The total price of the laptop is $' + str(total_amount))

# ex.7
# In a company the monthly salary of an employee is calculated by minimum wage 400$ per month, plus 20$ multiply by the employment years, plus 30$ for each employee kid.

# Create a program that:
# * Read the employment years
# * Read the number of each employee kids
# * Prints the total amount the employee must take
# * Output: "The total amount is 560$, 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids"

employment_years = 5
employee_kids = 2
minimum_wage = 400
employment_multiplier = 20
employment_bonus = employment_years * employment_multiplier
kid_multiplier = 30
kid_bonus = employee_kids * kid_multiplier
total_amount = minimum_wage + employment_bonus + kid_bonus
print(total_amount)
print('The total amount is ' + str(total_amount) + '$, ' + str(minimum_wage) + '$ minimum wage + ' + str(employment_bonus) + '$ for ' + str(employment_years) + ' years experience + ' + str(kid_bonus) + '$ for ' + str(employee_kids) + ' kids.')

# ex.8
# The exercise is almost identical to a previous exercise with a minor change. In a company the monthly salary of an employee is calculated by minimum wage 400$ per month, plus 20$ multiply by the employment years, plus 30$ for each employee kid, plus 100$ if the employee didn't miss 1 day of work.

# Create a program that:
# * Reads the employment years
# * Reads the number of each employee kids
# * Prints the total amount the employee must take
# * Output: "The total amount is 660$, 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids + 100$ for not missing a day at work"
# 
attendance_bonus = 100
print('employment years: ' + str(employment_years))
print('employee kids: ' + str(employee_kids))
new_total_amount = total_amount + attendance_bonus
print(new_total_amount)
print('The total amount is ' + str(new_total_amount) + '$, ' + str(minimum_wage) + '$ minimum wage + ' + str(attendance_bonus) + '$ for ' + str(employment_years) + ' years experience + ' + str(kid_bonus) + '$ for ' + str(employee_kids) + ' kids + ' + str(attendance_bonus) + '$ for not missing a day at work.')


# ex.9
# The exercise is almost identical to a previous exercise with a minor change. It's the end of the semester and you got your marks from, Geometry, Algebra, Physics classes. If the average score is 7 and above print "Good job!", if the average score is between 6 and 4 print "You need to work harder!", if the average score is below 4 print "Failed, you really need to work harder!".

# Create a program that:
# * Reads the values of these 3 lessons
# * Calculate the average of your grades
# * Example: Geometry = 6, Algebra = 7, Physics = 8
# * Output: Your average score is 7, Good job!"

# Warning! Do not use the programming language magic. After you complete the exercise feel free to do so.
# 
# 
if average_score > 7:
  print('Good Job!')
elif average_score > 4 and average_score < 6:
  print('You need to work harder!')
else:
  print('Failed, you really need to work harder')


# ex.10
# Create a program that prints the last digit of an integer

# Create a program that:
# * Reads an integer
# * Print the last digit

# Warning! Do not use the programming language magic. After you complete the exercise feel free to do so.

# Warning! Don't try to convert the number into string etc.

# Warning! For this problem it's ok after spending some time to look for the solution.

number = 18
print(number)
print(number % 10)

