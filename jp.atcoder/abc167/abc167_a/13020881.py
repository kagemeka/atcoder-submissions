import sys

s, t = sys.stdin.read().split()

def main():
    ans = "Yes" if t[:-1] == s else 'No'
    print(ans)

if __name__ == '__main__':
    main()
