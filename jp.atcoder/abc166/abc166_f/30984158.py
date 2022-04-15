def main() -> None:
    n, *a = map(int, input().split())
    # greedy
    strings = [input() for _ in range(n)]

    # corner case: sum(a) == 2
    # [1, 1, 0] -> which to transit [2, 0, 0] or [0, 2, 0] ?

    commands = [0 if s == "AB" else 1 if s == "BC" else 2 for s in strings]
    result = []
    for k in range(n):
        i = commands[k]
        j = (i + 1) % 3
        if a[i] > a[j]:
            result.append(j)
            a[i] -= 1
            a[j] += 1
        elif a[i] < a[j]:
            result.append(i)
            a[i] += 1
            a[j] -= 1
        elif a[i] == 0:
            print("No")
            return
        else:
            if k == n - 1 or commands[k + 1] == i or commands[k + 1] == (i - 1) % 3:
                a[i] += 1
                a[j] -= 1
                result.append(i)
            else:
                a[i] -= 1
                a[j] += 1
                result.append(j)

    abc = "ABC"
    print("Yes")
    print(*(abc[i] for i in result), sep="\n")


if __name__ == "__main__":
    main()
