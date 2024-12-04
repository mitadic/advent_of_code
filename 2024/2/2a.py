"""
analyze each row to validate its safety according to criteria
"""

INCR = 1
DECR = -1

def is_valid_report(report):
    order = INCR
    if report[0] > report[1]:
        order = DECR
    prev = -1
    for val in report:
        if prev == -1:
            prev = val
            continue
        if order == INCR and (val <= prev or val - prev > 3):
                return False
        elif order == DECR and (val >= prev or prev - val > 3):
                return False
        prev = val
    return True

def main():
    safe_count = 0
    with open('input') as f:
        rows = f.readlines()
    for row in rows:
        report = [int(x) for x in row.split()]
        if is_valid_report(report):
            # print(report)
            safe_count += 1
    print(safe_count)

if __name__ == '__main__':
    main()