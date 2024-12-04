
def similarity(l1, l2):
    score = 0
    for n1 in l1:
        for n2 in l2:
            if n2 == n1:
                score += n2
    return score

def main():
    l1 = []
    l2 = []
    with open('input') as f:
        rows = f.readlines()
    for row in rows:
        split = row.split(' ', 1)
        l1.append(int(split[0]))
        l2.append(int(split[1]))
    print(similarity(l1, l2))


if __name__ == "__main__":
    main()