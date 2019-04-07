#BRR
#MSAW

"""
You are given 2 out of 3 of the angles in a triangle, in degrees.

Write a function that classifies the missing angle as either "acute", "right", or "obtuse" based on its degrees.

An acute angle is one smaller than 90 degrees.
A right angle is one that is exactly 90 degrees.
An obtuse angle is one greater than 90 degrees (but smaller than 180 degrees).

"""


def missing_angle(angle1, angle2):
	if 180-(angle1+angle2)<90:
		return "acute"
	elif 180-(angle1+angle2)==90:
		return "right"
	else:
		return "obtuse"

	
"""
Create a function that takes a number as an argument and returns the amount of digits it has.

Examples
find_digit_amount(123) ➞ 3

find_digit_amount(56) ➞ 2

find_digit_amount(7154) ➞ 4

find_digit_amount(61217311514) ➞ 11

find_digit_amount(0) ➞ 1
"""
def find_digit_amount(num):
  string = str(num)
  length = len(string)
  return length


"""Create a function that takes a list of numbers and returns a new list, sorted in ascending order (smallest to biggest).

Sort numbers list in ascending order.
If function's argument is an empty list, return an empty list.
Return a new list of sorted numbers."""

def sortNumsAscending(lst):
	return sorted(lst)
