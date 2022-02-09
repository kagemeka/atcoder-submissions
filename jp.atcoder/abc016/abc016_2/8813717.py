import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    res1 = False
    if a + b == c:
        res1 =  True

    res2 = False
    if a - b == c:
        res2 =  True

    if res1 and res2:
        return '?'
    elif res1:
        return '+'
    elif res2:
        return '-'
    else:
        return '!'

if __name__ == '__main__':
    ans = main()
    print(ans)
