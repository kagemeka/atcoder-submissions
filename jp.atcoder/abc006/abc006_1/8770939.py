import sys

n = sys.stdin.readline().rstrip()

def main():
    if '3' in set(n) or int(n) % 3 == 0:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)
if __name__ == '__main__':
    main()
