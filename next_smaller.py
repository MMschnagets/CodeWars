def next_smaller(n):
    digits = list(str(n))
    length = len(digits)
    if length > 1:
        if digits[1] == '0' and list(str(n).replace(digits[1], '')) == sorted(list(str(n).replace(digits[1], ''))):
            return -1
    pivot_idx = -1
    for i in range(length - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            pivot_idx = i - 1
            break
    if pivot_idx == -1:
        return -1
    swap_idx = -1
    for i in range(length - 1, pivot_idx, -1):
        if digits[i] < digits[pivot_idx]:
            swap_idx = i
            break
    digits[pivot_idx], digits[swap_idx] = digits[swap_idx], digits[pivot_idx]
    digits[pivot_idx + 1:] = sorted(digits[pivot_idx + 1:], reverse=True)
    next_small = int(''.join(digits))
    return next_small


print(next_smaller(1027))
