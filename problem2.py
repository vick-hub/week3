import os
import sys


def main():
    x1 = int(input("x1; "))
    x2 = int(input("x2; "))
    x3 = int(input("x3; "))
    x4 = int(input("x4; "))
    y1 = int(input("y1; "))
    y2 = int(input("y2; "))
    y3 = int(input("y3; "))
    y4 = int(input("y4; "))
    x = [[x1, x2], [x3, x4]]
    y = [[y1, y2], [y3, y4]]
    p = [(x[0][0] * y[0][0] + x[0][1] * y[1][0]), (x[0][0]*y[0][1] + x[0][1]*y[1][1])], [(x[1][0]*y[0][0] + x[1][1]*y[1][0]), (x[1][0]*y[0][1] + x[1][1]*y[1][1])]
    print(f" p = {p}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
