import sys

n, m = map(int, sys.stdin.readline().split())

def main():
    if n >= m // 2: res = m // 2
    else: res = n + (m - 2 * n) // 4
    print(res)

if __name__ ==  '__main__':
    main()
