import sys
def main():
    n, l = map(int, sys.stdin.readline().split())
    amidakuji = [' ' + sys.stdin.readline().rstrip() + ' ' for _ in range(l)]
    goal = ' ' + sys.stdin.readline().rstrip()
    cur = goal.index('o')

    for i in range(l-1, -1, -1):
        if amidakuji[i][cur-1] == '-':
            cur -= 2
        elif amidakuji[i][cur+1] == '-':
            cur += 2

    start = (cur + 1) // 2
    print(start)

if __name__ == '__main__':
    main()
