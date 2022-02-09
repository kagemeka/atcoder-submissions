import sys

def main():
    x = int(sys.stdin.readline().rstrip())

    payable = [False] * (x + 1)
    payable[0] = True

    if x < 100:
        print(0)
        sys.exit()
    if 100 <= x <= 105:
        print(1)
        sys.exit()

    for i in range(100,106):
        payable[i] = True
    for i in range(106, x+1):
        payable[i] =  any(payable[i-105:i-99])

    print(payable[x] & 1)

if __name__ == '__main__':
    main()
