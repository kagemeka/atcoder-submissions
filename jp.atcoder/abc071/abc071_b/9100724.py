import sys
from string import ascii_lowercase

s = sys.stdin.readline().rstrip()

def main():
    res = sorted(set(ascii_lowercase) - set(s))
    return res[0] if res else None

if __name__ == '__main__':
    ans = main()
    print(ans)
