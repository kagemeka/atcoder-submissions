import typing



def main() -> typing.NoReturn:
    # a > 0
    # a > b >= -200
    # brute force

    x = int(input())

    k = 1
    while pow(k, 5) - pow(k - 1, 5) <= x: k += 1

    for a in range(1, k):
        for b in range(-k, a):
            if pow(a, 5) - pow(b, 5) != x: continue
            print(a, b)
            return


main()
