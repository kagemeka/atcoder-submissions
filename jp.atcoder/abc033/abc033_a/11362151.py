import sys

n = sys.stdin.readline().rstrip()

def main():
    ans = 'SAME' if len(set(n)) == 1 else 'DIFFERENT'
    print(ans)

if __name__ ==  '__main__':
    main()
