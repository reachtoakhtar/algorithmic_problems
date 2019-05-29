def spiral_order(lst):
    ret = []
    dir = 0

    top = 0
    bottom = len(lst) - 1

    left = 0
    right = len(lst[0]) - 1

    while left <= right and top <= bottom:
        if dir == 0:
            ret += [lst[top][i] for i in range(left, right + 1)]
            top += 1

        elif dir == 1:
            ret += [lst[i][right] for i in range(top, bottom + 1)]
            right -= 1

        elif dir == 2:
            ret += [lst[bottom][i] for i in reversed(range(left, right + 1))]
            bottom -= 1

        elif dir == 3:
            ret += [lst[i][left] for i in reversed(range(top, bottom + 1))]
            left += 1

        dir = (dir + 1) % 4

    return ret

