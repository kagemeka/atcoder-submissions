import sys

*a, = map(int, sys.stdin.readline().split())
a.sort()
a, b, c = a

def main():
    if a == b != c or a != b == c:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
