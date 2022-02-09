import sys

s = sys.stdin.readline().rstrip()

def main():
    l = len(s)
    if (l & 1) ^ (s[0] == s[-1]):
        return 'First'
    return 'Second'

if __name__ == '__main__':
    ans = main()
    print(ans)
