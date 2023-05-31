import bisect


def dbl_linear(n):
    list_temp = [1]
    set_temp = {1}
    count = 0
    while count < n:
        x = list_temp[count]
        y1 = 2 * x + 1
        y2 = 3 * x + 1
        if y1 not in set_temp:
            bisect.insort(list_temp, y1)
            set_temp.add(y1)
        if y2 not in set_temp:
            bisect.insort(list_temp, y2)
            set_temp.add(y2)
        count += 1
    return list_temp[n]


print(dbl_linear(10))
