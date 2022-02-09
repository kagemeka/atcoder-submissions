import sys

s, i = sys.stdin.read().split()
i = int(i)

def main():
    return s[i-1]

if __name__ == '__main__':
    ans = main()
    print(ans)
