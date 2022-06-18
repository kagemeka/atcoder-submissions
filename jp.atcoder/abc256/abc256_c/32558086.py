# mypy: ignore-errors

import sys

sys.setrecursionlimit(10**6)


def main() -> None:
    # reverse smallest in each cycle
    n = 3
    I = list(map(int, input().split()))
    h = I[:3]
    w = I[3:]

    # 30^4
    cnt = 0
    for a00 in range(1, 30):
        for a01 in range(1, 30):
            for a10 in range(1, 30):
                for a11 in range(1, 30):
                    a02 = h[0] - a00 - a01
                    a12 = h[1] - a10 - a11
                    a20 = w[0] - a00 - a10
                    a21 = w[1] - a01 - a11
                    a22 = w[2] - a02 - a12
                    # print(a02, a12, a20, a21, a22)
                    if a20 + a21 + a22 != h[2]:
                        continue
                    cnt += a02 >= 1 and a12 >= 1 and a20 >= 1 and a21 >= 1 and a22 >= 1
    print(cnt)


if __name__ == "__main__":
    main()
