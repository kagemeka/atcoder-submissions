import sys

a, b = map(int, sys.stdin.readline().split())


def main():
    print((a + b) % 24)


if __name__ == "__main__":
    main()
