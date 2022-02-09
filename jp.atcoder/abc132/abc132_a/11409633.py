import sys

s = sys.stdin.readline().rstrip()
s = sorted(s)

def main():
    ans = 'Yes' if s[0] == s[1] and s[2] == s[3] and s[1] != s[2] else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
