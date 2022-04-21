import math


def main() -> None:
    # volume of torus
    # (pi)r^2 * 2(pi)R
    r, d = map(int, input().split())
    v = math.pi * r**2 * 2 * math.pi * d
    print(v)


if __name__ == "__main__":
    main()
