import sys

a, b, c = sys.stdin.readline().split()

def main():
    return 'YES' if a[-1] == b[0] and b[-1] == c[0] else 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
