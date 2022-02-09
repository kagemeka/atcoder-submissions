import typing


def f(x: int) -> int:
    return x ** 2 + 2 * x + 3

def main() -> None:
    t = int(input())
    print(f(f(f(t) + t) + f(f(t))))



main()
