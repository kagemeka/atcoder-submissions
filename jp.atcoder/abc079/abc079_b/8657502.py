import sys

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-2) + lucas(n-1)

def main():
    n = int(sys.stdin.readline().rstrip())
    print(lucas(n))

if __name__ == "__main__":
    main()
