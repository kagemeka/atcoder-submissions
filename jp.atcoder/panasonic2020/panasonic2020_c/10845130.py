import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    if c - a - b <= 2:
        return 'No'
    l = 4 * a * b
    r = pow(c - a - b, 2)
    return 'Yes' if r > l else 'No'

if __name__ == "__main__":
    ans = main()
    print(ans)
