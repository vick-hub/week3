import os
import sys


def main():
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    x3 = int(input("x3: "))
    x4 = int(input("x4: "))
    x5 = int(input("x5: "))
    x6 = int(input("x6: "))
    x7 = int(input("x7: "))
    x8 = int(input("x8: "))
    x9 = int(input("x9: "))
    y1 = int(input("y1: "))
    y2 = int(input("y2: "))
    y3 = int(input("y3: "))
    y4 = int(input("y4: "))
    y5 = int(input("y5: "))
    y6 = int(input("y6: "))
    y7 = int(input("y7: "))
    y8 = int(input("y8: "))
    y9 = int(input("y9: "))
    x = [[x1, x2, x3], [x4, x5, x6], [x7, x8, x9]]
    y = [[y1, y2, y3], [y4, y5, y6], [y7, y8, y9]]
    p = [(x[0][0]*y[0][0]+x[0][1]*y[1][0]+x[0][2]*y[2][0]), (x[0][0]*y[0][1]+x[0][1]*y[1][1]+x[0][2]*y[2][1]),
         (x[0][0]*y[0][2]+x[0][1]*y[1][2]+x[0][2]*y[2][2])], [(x[1][0]*y[0][0]+x[1][1]*y[1][0]+x[1][2]*y[2][0]),
          (x[1][0]*y[0][1]+x[1][1]*y[1][1]+x[1][2]*y[2][1]), (x[1][0]*y[0][2]+x[1][1]*y[1][2]+x[1][2]*y[2][2])], [(x[2][0]*y[0][0]+x[2][1]*y[1][0]+x[2][2]*y[2][0]), (x[2][0]*y[0][1]+x[2][1]*y[1][1]+x[2][2]*y[2][1]), (x[2][0]*y[0][2]+x[2][1]*y[1][2]+
        x[2][2]*y[2][2])]
    print(f"p = {p}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
