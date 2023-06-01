from itertools import permutations, chain


def solve_puzzle(clues):
    size = 4
    for poss in permutations(permutations(range(1, size + 1), size), size):
        for i in range(size):
            if len(set(row[i] for row in poss)) < size:
                break
        else:
            cols_top = [[row[i] for row in poss] for i in range(size)]
            rows_right = [list(reversed(row)) for row in poss]
            cols_btm = [[row[i] for row in reversed(poss)] for i in reversed(range(size))]
            rows_left = list(reversed(poss))
            for i, row in enumerate(chain(cols_top, rows_right, cols_btm, rows_left)):
                if not clues[i]:
                    continue
                visible = 0
                for j, v in enumerate(row):
                    visible += v >= max(row[:j + 1])
                if visible != clues[i]:
                    break
            else:
                return poss


print(solve_puzzle((2, 2, 1, 3,
                    2, 2, 3, 1,
                    1, 2, 2, 3,
                    3, 2, 1, 3)))
