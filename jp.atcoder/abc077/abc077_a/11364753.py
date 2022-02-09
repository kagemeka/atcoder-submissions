import sys

s = sys.stdin.read().split()

def main():
    ans = 'YES' if s[0] == s[1][::-1] else 'NO'
    print(ans)

if __name__ ==  '__main__':
    main()
