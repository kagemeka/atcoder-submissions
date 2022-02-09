# 2019-11-22 22:30:40(JST)
import sys


def main():
    s = sys.stdin.readline().rstrip()


    end = ['ch', 'o', 'k', 'u']
    for char in end:
        s = s.replace(char, '')
    if s:
        ans = 'NO'
    else:
        ans = 'YES'

    print(ans)

if __name__ == '__main__':
    main()
