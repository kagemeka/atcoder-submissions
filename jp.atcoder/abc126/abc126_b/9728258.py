import sys

s = sys.stdin.readline().rstrip()

def main():
    a, b = int(s[:2]), int(s[2:])
    if 1 <= a <= 12:
        if 1 <= b <= 12:
            return 'AMBIGUOUS'
        else:
            return 'MMYY'
    else:
        if 1 <= b <= 12:
            return 'YYMM'
        else:
            return 'NA'

if __name__ == '__main__':
    ans = main()
    print(ans)
