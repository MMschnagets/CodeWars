def next_bigger(n):
    if n < 10:
        return -1
    print(n)
    str_n = str(n)
    length = len(str_n)
    if sorted(str_n, reverse=True) == list(str_n):
        return -1
    elif list(str_n).count(list(str_n)[0]) == length:
        return -1
    dict_unique = {k: str_n.count(k) for k in str_n}
    x = n + 1
    while x < pow(10, length):
        str_x = str(x)
        count_of_digits = 0
        for k in dict_unique.keys():
            if dict_unique.get(k) == str_x.count(k):
                count_of_digits += str_x.count(k)
        if count_of_digits == length:
            return x
        x += 1
    return -1


print(next_bigger(999999999))
