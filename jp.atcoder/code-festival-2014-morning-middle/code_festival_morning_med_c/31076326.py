import numpy as np


def main() -> None:
    p, n = input().split()
    p = float(p)
    n = int(n)

    a = np.array(
        [
            [1 - 2 * p, 0, p],
            [1, 0, 0],
            [0, 0, 1],
        ]
    )
    b = np.identity(3, dtype=np.float64)
    while n:
        if n & 1:
            b = b.dot(a)
        a = a.dot(a)
        n >>= 1
    c = np.array([p, 0, 1])
    print(b.dot(c)[1])


if __name__ == "__main__":
    main()
