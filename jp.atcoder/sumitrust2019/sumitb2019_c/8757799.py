import sys

payable = [False] * (10 ** 5 + 1)
payable[0] = True
for i in range(100,106):
    payable[i] = True

for i in range(106, 10 ** 5 + 1):
    payable[i] = any(payable[i-105:i-99])

def main():
    x = int(sys.stdin.readline().rstrip())
    print(payable[x] & 1)

if __name__ == '__main__':
    main()
