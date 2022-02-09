import sys

n, *h = map(int, sys.stdin.read().split())

def main():
    ans = 'Yes'
    for i in range(n - 1, 0, -1):
        if h[i-1] > h[i]: h[i-1] -= 1
        if h[i-1] > h[i]: ans = 'No'; break
    print(ans)

if __name__ ==  '__main__':
    main()
