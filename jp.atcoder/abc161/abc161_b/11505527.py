import sys

n, m, *a = map(int, sys.stdin.read().split())

def main():
    a.sort(reverse=True)
    s = sum(a)
    ans = 'Yes' if  a[m-1] * 4 * m >= s else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
