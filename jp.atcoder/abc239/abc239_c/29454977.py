def main() -> None:
    x0, y0, x1, y1 = map(int, input().split())

    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if abs(dx) + abs(dy) != 3:
                continue
            assert dx != 0 and dy != 0
            x = x0 + dx
            y = y0 + dy
            x = abs(x1 - x)
            y = abs(y1 - y)
            if x + y != 3:
                continue
            if x == 0 or y == 0:
                continue
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
