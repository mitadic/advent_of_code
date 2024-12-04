"""
sort two lists of numbers, then sum the differences of the
corresponding element values (int) on each row
"""

def sum_diffs(l1, l2):
    l1.sort()
    l2.sort()
    return sum(abs(a - b) for a, b in zip(l1, l2))

def main():
    l1 = []
    l2 = []
    with open('input') as f:
        rows = f.readlines()
    for row in rows:
        split = row.split(' ', 1)
        l1.append(int(split[0]))
        l2.append(int(split[1]))
    print(sum_diffs(l1, l2))

if __name__ == '__main__':
    main()