import sys

n = sys.stdin.readline().rstrip()

def main():
    ans = 'Yes' if '9' in set(n) else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
