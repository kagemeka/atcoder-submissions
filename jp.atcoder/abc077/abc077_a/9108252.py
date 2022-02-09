import sys

s1, s2 = sys.stdin.read().split()

def main():
    return 'YES' if s1[::-1] == s2 else 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
