"""
analyze each row to validate its safety according to criteria
"""

INCR = 1
DECR = -1

# 71 69 70 72 73 75 76

def order_mostly_decr(report):
    scale = 0
    prev = -1
    for val in report:
        if prev == -1:
            prev = val
            continue
        if prev > val:
            scale += 1
        prev = val
    # print(f"scale: {scale}, report: {report}")
    if scale >= (len(report) / 2):
        return True
    return False



def is_valid_report(report):
    dampener = True
    order = INCR
    if order_mostly_decr(report):
        order = DECR
    prev = -1
    for val in report:
        if prev == -1:
            prev = val
            continue
        if order == INCR and (val <= prev or val - prev > 3):
            print(val)
            if not dampener:
                print(f"report: {report}, val: {val}, order: INCR")
                return False
            dampener = False
            continue
        elif order == DECR and (val >= prev or prev - val > 3):
            if not dampener:
                print(f"report: {report}, val: {val}, order: DECR")
                return False
            dampener = False
            continue
        prev = val
    return True

def main():
    safe_count = 0
    with open('edge') as f:
        rows = f.readlines()
    for row in rows:
        report = [int(x) for x in row.split()]
        if is_valid_report(report):
            # print(report)
            safe_count += 1
    print(safe_count)

if __name__ == '__main__':
    main()