
__author__ = "akhtar"


def binary_search(array, item):
    first = 0
    last = len(array) - 1
    found = False
    midpoint = -1

    while first <= last and not found:
        midpoint = (first + last) // 2

        if array[midpoint] == item:
            found = True
        else:
            if item < array[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return midpoint if found else -1
