import sys

n, a, b, k, *p = map(int, sys.stdin.read().split())

def main():
    res = set(p)
    if a in res or b in res:
        return 'NO'
    elif len(res) != len(p):
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    ans = main()
    print(ans)
