# 2019-11-25 12:34:24(JST)
import sys
def main():
    *abc, = map(int, sys.stdin.readline().split())
    print(sorted(abc)[1])

if __name__ == '__main__':
    main()
