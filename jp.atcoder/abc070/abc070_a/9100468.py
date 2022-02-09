import sys

s = sys.stdin.readline().rstrip()

def main():
    return 'Yes' if s[::-1] == s else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
