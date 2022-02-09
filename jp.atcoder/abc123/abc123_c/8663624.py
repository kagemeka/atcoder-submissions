import sys
from math import ceil

def main():
    n, *capacity = map(int, sys.stdin.read().split())

    max_peop = n
    time = 0
    for c in capacity:
        time += ceil(max_peop / c)
        if max_peop > c:
            max_peop = c

    print(time)
if __name__ == "__main__":
    main()
