
__author__ = "akhtar"


def binary_search_iterative(array, item):
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


def binary_search_recursive(array, item, start, end):
    if end - start + 1 < 0:
        return -1
    else:
        midpoint = start + (end - start)//2
        if array[midpoint] == item:
            return midpoint
        else:
            if item < array[midpoint]:
                return binary_search_recursive(array, item, start, midpoint-1)
            else:
                return binary_search_recursive(array, item, midpoint+1, end)
