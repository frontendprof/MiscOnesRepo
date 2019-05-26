#BRR
#MSAW

"""
1)
You are given 2 out of 3 of the angles in a triangle, in degrees.

Write a function that classifies the missing angle as either "acute", "right", or "obtuse" based on its degrees.

An acute angle is one smaller than 90 degrees.
A right angle is one that is exactly 90 degrees.
An obtuse angle is one greater than 90 degrees (but smaller than 180 degrees).

"""



2)
	
"""
Create a function that takes a number as an argument and returns the amount of digits it has.

Examples
find_digit_amount(123) ➞ 3

find_digit_amount(56) ➞ 2

find_digit_amount(7154) ➞ 4

find_digit_amount(61217311514) ➞ 11

find_digit_amount(0) ➞ 1

"""

3)

"""Create a function that takes a list of numbers and returns a new list, sorted in ascending order (smallest to biggest).

Sort numbers list in ascending order.
If function's argument is an empty list, return an empty list.
Return a new list of sorted numbers.

"""


4)
"""
Create a function that takes a single string as an argument and returns an ordered list containing the indexes of all capital letters in the string.
Examples
indexOfCaps("eDaBiT") ➞ [1, 3, 5]

indexOfCaps("eQuINoX") ➞ [1, 3, 4, 6]

indexOfCaps("determine") ➞ []

indexOfCaps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]

indexOfCaps("sUn") ➞ [1]

"""






















1)
"""
def missing_angle(angle1, angle2):
	if 180-(angle1+angle2)<90:
		return "acute"
	elif 180-(angle1+angle2)==90:
		return "right"
	else:
		return "obtuse"
	
"""

2)
"""
def find_digit_amount(num):
  string = str(num)
  length = len(string)
  return length
  
"""

3)
"""
def sortNumsAscending(lst):
	return sorted(lst)
"""

4)
"""

a)
def indexOfCaps(word):
	return [i for i in range(len(word)) if word[i].isupper()]
b)
result=list()
for i in word:
   if i.isupper():
      result.append(word.index(i))
return result
"""

