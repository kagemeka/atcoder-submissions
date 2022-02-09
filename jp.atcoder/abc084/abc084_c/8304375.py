import sys
# import collections
# import math
# import string
# import bisect
# import re
# import itertools
# import statistics

def main():
    n = int(sys.stdin.readline().rstrip())
    c, s, f = [], [], []
    for i in range(n-1):
        ci, si, fi = (int(x) for x in sys.stdin.readline().split())
        c.append(ci); s.append(si); f.append(fi)

    x = []
    for i in range(n-1):
        xi = 0
        for j in range(i, n-1):
            if s[j] >= xi:
                xi = s[j]
                xi += c[j]
            else:
                if (xi - s[j]) % f[j] == 0:
                    xi += c[j]
                else:
                    xi += c[j] + f[j] - (xi - s[j]) % f[j]
        x.append(xi)
    x.append(0)
    for xi in x:
        print(xi)

if __name__ == "__main__":
    # execute only if run as a script
    main()

# 乗り換え時間がなく、一方通行の電車!
