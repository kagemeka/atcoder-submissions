import sys

s = sys.stdin.readline().rstrip()

def main():
    return 'Yes' if s[:3] == s[0] * 3 or s[1:] == s[-1] * 3 else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
