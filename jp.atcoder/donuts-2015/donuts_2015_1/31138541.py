def compute_volume(x0: float, r: float) -> float:
    import math

    return 2 * math.pi**2 * r**2 * x0


def main() -> None:
    # volume of torus
    # (pi)r^2 * 2(pi)R
    r, d = map(int, input().split())
    print(compute_volume(d, r))


if __name__ == "__main__":
    main()
