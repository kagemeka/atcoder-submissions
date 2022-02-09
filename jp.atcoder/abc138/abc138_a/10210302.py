import sys

a, s = sys.stdin.read().split()
a = int(a)

def main():
    return s if a >= 3200 else 'red'

if __name__ == '__main__':
    ans = main()
    print(ans)
