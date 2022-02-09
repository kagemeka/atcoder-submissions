import typing


def main() -> None:
    MOD = 998_244_353
    n = int(input())
    d = 1
    s = 0
    for i in range(18):
        if n >= d * 10:
            c = d * 9
            s += (1 + c) * c // 2
            s %= MOD
        else:
            c = n - d + 1
            s += (1 + c) * c // 2
            s %= MOD
            break
        d *= 10
    print(s)


if __name__ == "__main__":
    main()
