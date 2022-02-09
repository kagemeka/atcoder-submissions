import sys

s = sys.stdin.readline().rstrip()

def main():
    return 'yes' if len(set(s)) == len(s) else 'no'

if __name__ == '__main__':
    ans = main()
    print(ans)
