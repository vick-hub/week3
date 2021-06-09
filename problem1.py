import os
import sys
import random


def main():
    x = random.sample(range(0, 9), 5)
    print(x)
    y = int(input("y: "))
    print(f" y = {y not in x}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
