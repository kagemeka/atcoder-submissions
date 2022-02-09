import sys

n = int(sys.stdin.readline().rstrip())

def base_convert(n, base):
    res = []
    b = abs(base)
    while n:
        q, r = divmod(n, b)
        res.append(r)
        n = b * q // base
    try:
        return int(''.join(list(map(str, res)))[::-1])
    except:
        return 0

def main():
    return base_convert(n, -2)

if __name__ == '__main__':
    ans = main()
    print(ans)
