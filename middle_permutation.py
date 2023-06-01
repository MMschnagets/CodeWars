import math


def middle_permutation(s):
    sorted_s = sorted(s)
    n = len(s)
    mid_index = math.factorial(n) // 2 - 1
    result = []
    while n > 0:
        index, mid_index = divmod(mid_index, math.factorial(n - 1))
        result.append(sorted_s.pop(index))
        n -= 1
    return ''.join(result)


print(middle_permutation('abcd'))
