import sys

s, t = sys.stdin.read().split()
s *= 2

def main():
    n = len(t)
    for i in range(n):
        if s[i:i+n] == t:
            return 'Yes'
    return 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
