import sys

s = sys.stdin.readline().rstrip()

def main():
    return s[::2]

if __name__ == '__main__':
    ans = main()
    print(ans)
