import sys

digits = set(sys.stdin.readline().rstrip())

def main():
    if len(digits) == 1:
        return 'SAME'
    return 'DIFFERENT'

if __name__ == '__main__':
    ans = main()
    print(ans)
