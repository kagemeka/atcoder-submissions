import sys
import math
import numpy as np

def main():
    dish = np.array(sys.stdin.read().split())

    minute = [int(dish[i][-1]) for i in range(5)]
    m = min(x for x in minute if x > 0) if 0 in minute else 10

    res = (np.ceil(dish.astype(np.int64) / 10) * 10).sum() - 10 + m

    print(int(res))

if __name__ == "__main__":
    main()
