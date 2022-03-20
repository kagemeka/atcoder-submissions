def main() -> None:
    n = int(input())
    t = input()
    direction = 1
    x, y = 0, 0
    for c in t:
        if c == 'S':
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
        else:
            direction = (direction + 1) % 4
    print(x, y)


if __name__ == "__main__":
    main()
