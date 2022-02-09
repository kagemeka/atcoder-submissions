import sys

n = int(sys.stdin.readline().rstrip())

def base_convert(n, b):
    res = ''
    while n:
        r = abs(n % b)
        res = str(r) + res
        n = (n - r) // b

    return int(res) if res else 0

def main():
    return base_convert(n, 3)

if __name__ == '__main__':
    ans = main()
    print(ans)
