import os
import sys


def main():
    t = int(input("t: "))
    y = list(range(t))
    print(f" y = {y}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
