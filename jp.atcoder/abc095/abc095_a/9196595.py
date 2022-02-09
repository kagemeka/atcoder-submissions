import sys

s = sys.stdin.readline().rstrip()

def main():
    return 700 + 100 * s.count('o')

if __name__ == '__main__':
    ans = main()
    print(ans)
