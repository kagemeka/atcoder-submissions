import sys

n = sys.stdin.readline().rstrip()
hon = [2, 4, 5, 7, 9]
pon = [0, 1, 6, 8]
def main():
    d = int(n[-1])
    if d in hon:
        ans = 'hon'
    elif d in pon:
        ans = 'pon'
    else:
        ans = 'bon'
    print(ans)

if __name__ == '__main__':
    main()
