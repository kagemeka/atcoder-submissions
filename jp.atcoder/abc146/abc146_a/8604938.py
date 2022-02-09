# 2019-11-24 20:59:47(JST)
import sys
#import numpy as np

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
def main():
    s = sys.stdin.readline().rstrip()
    ans = 7 - days.index(s)
    print(ans)

if __name__ == '__main__':
    main()
