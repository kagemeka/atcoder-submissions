import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    res = set()
    for i in a:
        while not i & 1:
            i //= 2
        res.add(i)
    return len(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
