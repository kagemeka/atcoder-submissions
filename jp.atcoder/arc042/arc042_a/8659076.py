# 2019-11-26 14:51:37(JST)
import sys
from collections import defaultdict, OrderedDict

def main():
    n, m, *a = sys.stdin.read().split()

    order_latest = OrderedDict((thread, True) for thread in reversed(a))
    res = list(order_latest.keys())
    ans = res + sorted(set(range(1, int(n) + 1)) - set(map(int, res)))
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()
