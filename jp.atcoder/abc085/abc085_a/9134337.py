import sys

s = sys.stdin.readline().rstrip()

def main():
    return s[:3] + '8' + s[4:]

if __name__ == '__main__':
    ans = main()
    print(ans)
