
__author__ = "akhtar"


def decimal_to_binary(number):
    """ Convert a decimal number to its corresponding binary string. """

    s = []
    while number > 0:
        s.append(number%2)
        number = number // 2

    binary_string = ""
    while len(s) > 0:
        binary_string += str(s.pop())

    return binary_string

