import numpy as np
import sys


def main() -> None:
    c = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(3, 3)
    c -= c[0]
    c -= c[:, 0][:, None]
    print("Yes" if np.all(c == 0) else "No")


if __name__ == "__main__":
    main()
