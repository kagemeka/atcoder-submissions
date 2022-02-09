import sys

x = int(sys.stdin.readline().rstrip())

def main():
    q, r = divmod(x, 11)
    if r == 0:
        return 2 * q
    elif r <= 6:
        return 2 * q + 1
    else:
        return 2 * (q + 1)

if __name__ == '__main__':
    ans = main()
    print(ans)
