import sys

s = sys.stdin.readline().rstrip()
s = ''.join(sorted(s))

def main():
    ans = 'Yes' if s == 'abc' else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
