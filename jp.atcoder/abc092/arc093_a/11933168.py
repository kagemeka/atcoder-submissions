import sys

n, *a = map(int, sys.stdin.read().split())
a = [0] + a + [0]

def main():
    s = sum([abs(a[i+1] - a[i]) for i in range(n + 1)])
    for i in range(1, n + 1):
        if a[i-1] <= a[i] <= a[i+1]: res = s
        elif a[i-1] >= a[i] >= a[i+1]: res = s
        else: res = s - 2 * min(abs(a[i] - a[i-1]), abs(a[i+1] - a[i]))
        print(res)

if __name__ ==  '__main__':
    main()
