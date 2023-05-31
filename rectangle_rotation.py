from math import floor, sqrt


def rectangle_rotation(a, b):
    val_a, val_b = floor(a / sqrt(2)), floor(b / sqrt(2))
    val_a2, val_b2 = val_a, val_b
    if val_a % 2 == 0:
        val_a += 1
    else:
        val_a2 += 1

    if val_b % 2 == 0:
        val_b += 1
    else:
        val_b2 += 1

    result = val_a * val_b + val_a2 * val_b2
    return result


print(rectangle_rotation(8, 6))
