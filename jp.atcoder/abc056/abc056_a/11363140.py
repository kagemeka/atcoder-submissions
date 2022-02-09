import sys

def convert(x):
    return 1 if x == 'H' else 0

a, b = sys.stdin.readline().split()
a = convert(a)
b = convert(b)

def main():
    ans = 'D' if a ^ b else 'H'
    print(ans)

if __name__ ==  '__main__':
    main()
