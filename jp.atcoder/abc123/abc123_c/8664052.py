import sys
from math import ceil

def main():
    n, *capacity = map(int, sys.stdin.read().split())

    time = 0
    min_cap = capacity[0]
    for i in range(5):
        # 現時点で何人city i にいるか
        remain = n - (time - i) * min_cap
        time += ceil(remain / min_cap)
        min_cap = min(min_cap, capacity[i])

    print(time)
if __name__ == "__main__":
    main()
