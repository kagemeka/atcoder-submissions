import sys

a = '1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51'.split(', ')

k = int(sys.stdin.readline().rstrip())

def main():
    return a[k-1]

if __name__ == "__main__":
    ans = main()
    print(ans)