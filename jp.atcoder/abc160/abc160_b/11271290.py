import sys

x = int(sys.stdin.readline().rstrip())

def main():
    q, r = divmod(x, 500)
    res = q * 1000
    q, r = divmod(r, 5)
    res += 5 * q
    print(res)

if __name__ == "__main__":
    main()
