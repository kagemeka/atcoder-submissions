import sys

q = int(sys.stdin.readline().rstrip())

def main():
    if q == 1:
        return 'ABC'
    return 'chokudai'

if __name__ == '__main__':
    ans = main()
    print(ans)
