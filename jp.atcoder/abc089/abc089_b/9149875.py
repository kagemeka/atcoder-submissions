import sys

n, *s = sys.stdin.read().split()

def main():
    return 'Four' if len(set(s)) == 4 else 'Three'

if __name__ == '__main__':
    ans = main()
    print(ans)
