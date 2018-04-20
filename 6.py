
__author__ = "akhtar"


def pair_with_given_sum(lst, sum):
	""" Given an unsorted array, find a pair with given sum in it. """

	d = dict()
	for i in lst:
		val = d.get(sum-i)
		if val:
			print("Sum found: {}(index={}) and {}(index={})".format(i, lst.index(i), sum-i, val))
			return
		else:
			d[i] = lst.index(i)

	print("Sum not found.")


pair_with_given_sum([3, 2, 5, 4, 6, 9], 11)
