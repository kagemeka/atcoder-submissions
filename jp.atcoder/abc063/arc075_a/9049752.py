import sys

n, *s = map(int, sys.stdin.read().split())

def main():
    res = sum(s)
    if res % 10:
        return res
    else:
        not_multiple_of_10 = [x for x in s if x % 10]
        if not_multiple_of_10:
            return res - min(not_multiple_of_10)
        else:
            return 0

if __name__ == '__main__':
    ans = main()
    print(ans)
