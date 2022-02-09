import sys

u = set('753')
x = sys.stdin.readline().rstrip()

def main():
    ans = 'YES' if x in u else 'NO'
    print(ans)

if __name__ ==  '__main__':
    main()
