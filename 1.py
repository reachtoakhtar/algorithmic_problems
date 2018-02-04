import sys

__author__ = "akhtar"


def second_largest(lst):
	""" Find the 2nd largest element in an array. """

	first = -sys.maxsize - 1  # max=sys.maxsize
	second = -sys.maxsize - 1

	for element in lst:
		if element > first:
			second = first
			first = element
		elif element > second:
			second = element

	return second


print(second_largest([1, 4, 2, -8, 90]))
