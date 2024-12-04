"""
Find occurrences of MASxMAS:

M S
 A
M S

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........                  """


def is_mas(lines, l_idx, c_idx):
    """
    'A' was found at lines[l_idx][c_idx], now look at 2 diagonals & verify MAS
    """
    # early exit if out-of-bounds
    if ((l_idx - 1 < 0 or c_idx - 1 < 0) or
        (l_idx - 1 < 0 or c_idx + 1 >= len(lines[l_idx])) or
        (l_idx + 1 >= len(lines) or c_idx + 1 >= len(lines[l_idx])) or
        (l_idx + 1 >= len(lines) or c_idx - 1 < 0)
    ): return False
    
    # early exit if non-matching characters on the diagonals
    if ((lines[l_idx - 1][c_idx - 1] not in "MS") or
        (lines[l_idx - 1][c_idx + 1] not in "MS") or
        (lines[l_idx + 1][c_idx + 1] not in "MS") or
        (lines[l_idx + 1][c_idx - 1] not in "MS") 
    ): return False

    # NW - SE
    if lines[l_idx - 1][c_idx - 1] == 'M':
        if lines[l_idx + 1][c_idx + 1] != 'S':
            return False
    elif lines[l_idx - 1][c_idx - 1] == 'S':
        if lines[l_idx + 1][c_idx + 1] != 'M':
            return False
    # SW - NE
    if lines[l_idx - 1][c_idx + 1] == 'M':
        if lines[l_idx + 1][c_idx - 1] != 'S':
            return False
    elif lines[l_idx - 1][c_idx + 1] == 'S':
        if lines[l_idx + 1][c_idx - 1] != 'M':
            return False
    return True


def main():
    pattern_occurrences = 0
    with open('b_input', 'r') as f:
        lines = f.readlines()
    for l_idx in range(len(lines)):
        for c_idx in range(len(lines[l_idx])):
            if lines[l_idx][c_idx] == 'A':
                if is_mas(lines, l_idx, c_idx):
                    pattern_occurrences += 1
    print(pattern_occurrences)


if __name__ == '__main__':
    main()