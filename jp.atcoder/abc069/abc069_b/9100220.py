import sys

s = sys.stdin.readline().rstrip()
l = len(s)

def main():
    return s[0] + str(l-2) + s[-1]

if __name__ == '__main__':
    ans = main()
    print(ans)
