import sys

n = set(sys.stdin.readline().rstrip())

def main():
    return 'Yes' if '9' in n else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
