def validate_battlefield(field):
    ships = {}
    for row in range(len(field[0])):
        for col in range(len(field)):
            if field[row][col] == 1:
                try:
                    result = get_ship_size(row, col, field)
                    ships[result] = ships.get(result, 0) + 1
                except ValueError:
                    return False
    return ships.get(4, 0) == 1 and ships.get(3, 0) == 2 and ships.get(2, 0) == 3 and ships.get(1, 0) == 4


def is_corner_valid(row, col, field):
    if row == len(field) - 1:
        return True
    if col == 0:
        return field[row + 1][col + 1] != 1
    if col == len(field[0]) - 1:
        return field[row + 1][col - 1] != 1
    return field[row + 1][col + 1] != 1 and field[row + 1][col - 1] != 1


def is_side_valid(row, col, field):
    if row == len(field) - 1 or col == len(field[0]) - 1:
        return True
    return not (field[row + 1][col] != 0 and field[row][col + 1] != 0)


def is_valid_point(row, col, field):
    return is_corner_valid(row, col, field) and is_side_valid(row, col, field)


def get_ship_size(row, col, field):
    if not is_valid_point(row, col, field):
        raise ValueError('Invalid disposition')
    field[row][col] = -1
    if row != len(field) - 1 and field[row + 1][col] == 1:
        return 1 + get_ship_size(row + 1, col, field)
    if col != len(field[0]) - 1 and field[row][col + 1] == 1:
        return 1 + get_ship_size(row, col + 1, field)
    return 1


print(validate_battlefield([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                           [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                           [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
