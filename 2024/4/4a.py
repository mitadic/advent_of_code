"""
Find occurrences of XMAS (8-directional), as highlighted here:

..X...
.SAMX.
.A..A.
XMAS.S
.X....                  """

W = 0
NW = 1
N = 2
NE = 3
E = 4
SE = 5
S = 6
SW = 7

CHAR_X = 0
CHAR_M = 1
CHAR_A = 2
CHAR_S = 3
BEYOND_COMPLETION = 4

chars_dict = {
    0: 'X',
    1: 'M',
    2: 'A',
    3: 'S'
}


def xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum):
    if char_enum == BEYOND_COMPLETION:
        return True
    
    if dir == W:
        if c_idx - char_enum < 0:  # early exit this iteration
            return False
        if lines[l_idx][c_idx - char_enum] == chars_dict[char_enum]:
            return xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum + 1)
    if dir == NW:
        if l_idx - char_enum < 0 or c_idx - char_enum < 0:
            return False
        if lines[l_idx - char_enum][c_idx - char_enum] == chars_dict[char_enum]:
            return xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum + 1)
    if dir == N:
        if l_idx - char_enum < 0:
            return False
        if lines[l_idx - char_enum][c_idx] == chars_dict[char_enum]:
            return xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum + 1)
    if dir == NE:
        if l_idx - char_enum < 0 or c_idx + char_enum >= len(lines[l_idx]):
            return False
        if lines[l_idx - char_enum][c_idx + char_enum] == chars_dict[char_enum]:
            return xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum + 1)
    if dir == E:
        if c_idx + char_enum >= len(lines[l_idx]):
            return False
        if lines[l_idx][c_idx + char_enum] == chars_dict[char_enum]:
            return xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum + 1)
    if dir == SE:
        if l_idx + char_enum >= len(lines) or c_idx + char_enum >= len(lines[l_idx]):
            return False
        if lines[l_idx + char_enum][c_idx + char_enum] == chars_dict[char_enum]:
            return xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum + 1)
    if dir == S:
        if l_idx + char_enum >= len(lines):
            return False
        if lines[l_idx + char_enum][c_idx] == chars_dict[char_enum]:
            return xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum + 1)
    if dir == SW:
        if l_idx + char_enum >= len(lines) or c_idx - char_enum < 0:
            return False
        if lines[l_idx + char_enum][c_idx - char_enum] == chars_dict[char_enum]:
            return xmas_in_this_direction(lines, l_idx, c_idx, dir, char_enum + 1)
    return False


def how_many_xmasses(lines, l_idx, c_idx):
    """
    'X' was found at lines[l_idx][c_idx], now look in 8 directions and count
    """
    occurrences = 0
    for i in range(8):
        if xmas_in_this_direction(lines, l_idx, c_idx, i, CHAR_X):
            occurrences += 1
    return occurrences


def main():
    pattern_occurrences = 0
    with open('input', 'r') as f:
        lines = f.readlines()
    for l_idx in range(len(lines)):
        for c_idx in range(len(lines[l_idx])):
            if lines[l_idx][c_idx] == 'X':
                pattern_occurrences += how_many_xmasses(lines, l_idx, c_idx)
    print(pattern_occurrences)


if __name__ == '__main__':
    main()