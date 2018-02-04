import sys

__author__ = "akhtar"


def largest_subarray(lst):
	"""
	You have an array containing positive and negative numbers (no zeros).
	How will you find the sub-array with the largest sum?
	"""
	max_so_far = -sys.maxsize - 1
	max_ending_here = 0
	start = 0
	end = 0
	s = 0

	for i in range(0, len(lst)):
		max_ending_here += lst[i]

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

		if max_ending_here < 0:
			max_ending_here = 0
			s = i + 1

	print("Maximum contiguous sum is {0}".format(max_so_far))
	print("Starting and ending index of the subarray are {0}".format([start, end]))
	print("Subarray is {0}".format(lst[start:end+1]))


largest_subarray([1, 4, -6, 8, 1, -4, 5, -3, 1, -1, 6, -5])
