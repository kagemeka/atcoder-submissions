import sys
def main():
    s = sys.stdin.readline().rstrip()
    if s[-1] == 'T':
        ans = 'YES'
    else:
        ans = 'NO'
    print(ans)

if __name__ == '__main__':
    main()
