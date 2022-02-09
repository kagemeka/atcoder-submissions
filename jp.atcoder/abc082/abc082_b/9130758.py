import sys

s, t = sys.stdin.read().split()

def main():
    return 'Yes' if ''.join(sorted(s)) < ''.join(sorted(t))[::-1] else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
