import sys

a, b = sys.stdin.readline().split()
a = 1 if a == 'H' else 0
b = 1 if b == 'H' else 0

def main():
    return 'D' if a ^ b else 'H'

if __name__ == '__main__':
    ans = main()
    print(ans)
