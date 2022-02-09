import sys

x = int(sys.stdin.readline().rstrip())

def main():
    l = 0
    r = x + 1
    while l + 1 < r:
        m = (l + r) // 2
        if (1 + m) * m // 2 >= x:
            r = m
        else:
            l = m
    return r

if __name__ == '__main__':
    ans = main()
    print(ans)
