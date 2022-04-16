import math


def main() -> None:
    # if k == 1, infinity
    # if k >= 2
    # enumerate all lines passing each two coorinate pairs.
    # O(N^2)
    # for each line, check how many coodinates passing the line.

    # store katamuki(dx, dy) divided by gcd and y0 (when x = 0)
    # y0 (dx, y * dx - x * dy)
    n, k = map(int, input().split())
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    if k == 1:
        print("Infinity")
        return
    lines = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            xi, yi = xy[i]
            xj, yj = xy[j]
            dx = xj - xi
            dy = yj - yi
            if dx < 0:
                dx *= -1
                dy *= -1
            assert not dx == dy == 0
            g = math.gcd(dx, dy)
            dx //= g
            dy //= g
            if dx == 0 and dy < 0:
                dy *= -1
            if dy == 0 and dx < 0:
                dx *= -1
            y0 = None if dx == 0 else yi * dx - xi * dy
            x0 = None if dy == 0 else xi * dy - yi * dx
            # print(i, j, dx, dy, x0, y0, xi, yi)
            lines.append((dx, dy, x0, y0))

    # print(lines)

    lines = list(set(lines))
    tot = 0
    for line in lines:
        dx, dy, x0, y0 = line
        count = 0
        for x, y in xy:
            if y0 is None:
                count += x == x0
            elif x0 is None:
                count += y == y0
            else:
                count += y * dx - y0 == dy * x
        tot += count >= k
    print(tot)


if __name__ == "__main__":
    main()
