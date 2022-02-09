import sys

s = sys.stdin.readline().rstrip()

def main():
    ans = 'Yes' if len(set(s)) == 2 else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
