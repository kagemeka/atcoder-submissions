import sys

n = sys.stdin.readline().rstrip()

def main():
    ans = 'Yes' if n == n[::-1] else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
