import sys

s = sys.stdin.readline().rstrip()

def main():
    ans = 'YES' if s[-1] == 'T' else 'NO'
    print(ans)

if __name__ ==  '__main__':
    main()
