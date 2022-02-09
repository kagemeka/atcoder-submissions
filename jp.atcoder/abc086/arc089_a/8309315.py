#                         author:  kagemeka
#                         created: 2019-11-06 12:47:30(JST)
import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n, *txy = (int(x) for x in sys.stdin.read().split())
    t, x, y = [0], [0], [0]
    for i in range(0, n * 3, 3):
        t.append(txy[i])
        x.append(txy[i+1])
        y.append(txy[i+2])
    for i in range(n):
        dt = t[i+1] - t[i]
        distx = abs(x[i+1] - x[i])
        disty = abs(y[i+1] - y[i])
        if dt - (distx + disty) >= 0 and (dt - (distx + disty)) % 2 == 0:
            continue
        else:
            ans = 'No'
            break
    else:
        ans = 'Yes'

    print(ans)

if __name__ == "__main__":
    # execute only if run as a script
    main()
