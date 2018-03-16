
__author__ = "akhtar"


def par_checker(string):
    """ Check whether the input string contains a balanced set of parantheses. """

    s = []
    balanced = True
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]
        if symbol == "(":
            s.append(symbol)
        else:
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and len(s) == 0
