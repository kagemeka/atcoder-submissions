import sys

s = sys.stdin.readline().rstrip()

def main():
    if s[0] == s[1]:
        return 1, 2
    for i in range(1, len(s)-1):
        if s[i-1] == s[i+1]:
            return i, i+2
        elif s[i] == s[i+1]:
            return i+1, i+2

    return -1, -1

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
