import numpy as np
import sys


def main() -> None:
    n = int(sys.stdin.readline().rstrip())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    print(*(np.bitwise_xor.reduce(a) ^ a))


if __name__ == "__main__":
    main()
