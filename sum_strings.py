import itertools

def sum_strings(x, y):
    if x=='':
        if y=='':
            return '0'
        else:
            return y
    elif y=='':
        return x
    result = []
    carry = 0
    for digit_x, digit_y in itertools.zip_longest(reversed(x), reversed(y), fillvalue='0'):
        digit_sum = int(digit_x) + int(digit_y) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))
    if carry:
        result.append(str(carry))
    temp_str = ''.join(reversed(result))
    if len(temp_str)>1:
        return temp_str.removeprefix('0')
    return temp_str
