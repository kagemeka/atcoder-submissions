import bisect

def main() -> None:
    x, n = map(int, input().split())
    p = set(map(int, input().split()))

    for lo in range(x, x - n - 1, -1):
        if lo not in p:
            break

    for hi in range(x, x + n + 1):
        if hi not in p:
            break

    print(lo if x - lo <= hi - x else hi)





if __name__ == "__main__":
    main()
