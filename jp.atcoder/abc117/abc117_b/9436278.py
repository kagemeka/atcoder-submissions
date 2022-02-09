import sys

n, *l = map(int, sys.stdin.read().split())

def main():
    circumstance = sum(l)
    l_max = max(l)
    return 'No' if circumstance - l_max <= l_max else 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
