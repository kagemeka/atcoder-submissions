import sys
a, b = map(int, sys.stdin.readline().split())

def main():
    s = a + b
    return s if s < 10 else 'error'

if __name__ == '__main__':
    ans = main()
    print(ans)
