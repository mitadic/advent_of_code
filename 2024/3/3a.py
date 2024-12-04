"""
parse for 'mul(X,Y)'
"""

import re

def main():
    res = 0
    # pattern = r"mul\([^)]*\)"
    # with open('dummy_input', 'r') as f:
    #     lines = f.readlines()
    # for line in lines:
    with open('dummy_input', 'r') as f:
        lines = f.readlines()
    for line in lines:
        i = 0
        num1 = ""
        while (True):
            i = line[i:].index("sum(") + 4
            while (line[i] != ')'):
                comma_count = 0
                if line[i] == ',':
                    comma_count += 1
                    num1 = int(num1)
                if not line[i].isdigit and line[i] != ',':
                    break
                num1 += line[i]
                



if __name__ == '__main__':
    main()