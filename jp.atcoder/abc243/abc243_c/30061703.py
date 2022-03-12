def main() -> None:
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    s = input()

    xy = sorted(enumerate(xy), key=lambda v: (v[1][1], v[1][0]))
    prev_y = -1
    directions = []
    for i, (x, y) in xy:
        if y != prev_y:
            directions.append([])
        prev_y = y
        directions[-1].append(s[i])

    for d in directions:
        for i in range(len(d) - 1):
            if d[i] == "R" and d[i + 1] == "L":
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
