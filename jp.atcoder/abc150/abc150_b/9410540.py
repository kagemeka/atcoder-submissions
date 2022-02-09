import sys

n, s = sys.stdin.read().split()
n = int(n)

def main():
    return s.count('ABC')

if __name__ == '__main__':
    ans = main()
    print(ans)
