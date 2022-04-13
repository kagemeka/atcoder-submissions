def main() -> None:
    n = int(input()) - 1

    K = 26

    p = 1
    for i in range(20):
        p *= K
        if n >= p:
            n -= p
            continue
        res = []
        while n:
            n, r = divmod(n, K)
            res.append(chr(r + 97))
        print("a" * (i + 1 - len(res)) + "".join(res[::-1]))
        return


if __name__ == "__main__":
    main()
