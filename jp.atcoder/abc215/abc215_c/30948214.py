import itertools


def main() -> None:
    s, k = input().split()
    k = int(k)
    a = sorted(set(map(lambda x: "".join(x), itertools.permutations(s))))
    print(a[k - 1])


if __name__ == "__main__":
    main()
