def main() -> None:
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(l - sum(a))
    a.sort(reverse=True)
    if a[-1] == 0:
        a.pop()

    cost = l
    length = a[0]
    for x in a[1:-1]:
        c = l - length
        length += x
        cost += min(c, length)
    print(cost)


if __name__ == "__main__":
    main()
