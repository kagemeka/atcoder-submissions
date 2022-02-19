def main() -> None:
    x0, y0, x1, y1 = map(int, input().split())

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx) + abs(dy) != 3:
                continue
            if abs(dx) == 0 or abs(dy) == 0:
                continue
            x = x0 + dx
            y = y0 + dy
            dx = abs(x1 - x)
            dy = abs(y1 - y)
            if abs(dx) + abs(dy) != 3:
                continue
            if abs(dx) == 0 or abs(dy) == 0:
                continue
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
