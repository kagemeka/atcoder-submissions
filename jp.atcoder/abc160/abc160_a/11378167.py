import sys

s = sys.stdin.readline().rstrip()

def main():
    ans = 'Yes' if s[2] == s[3] and s[4] == s[5] else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
