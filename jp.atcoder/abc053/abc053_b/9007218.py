import sys

s = sys.stdin.readline().rstrip()

def main():
    a = s.index('A')
    z = len(s) - (s[::-1].index('Z') + 1)
    return z - a + 1

if __name__ == '__main__':
    ans = main()
    print(ans)
