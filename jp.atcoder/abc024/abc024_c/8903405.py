import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, d, k = I[:3]
I -= 1
lr = I[3:3+d*2].reshape(d, 2)
s, t = I[3+d*2:].reshape(k, 2).T

def main():

    arrival = np.full(k, np.inf)
    day = 0
    for l, r in lr:
        day += 1
        can_move = (l <= s) & (s <= r)
        into_dest = (l <= t) & (t <= r)
        can_arrive = can_move & into_dest

        s[can_move & (t < l)] = l
        s[can_arrive] = t[can_arrive]
        s[can_move & (t > r)] = r
        arrival[can_arrive] = np.minimum(arrival[can_arrive], day)

    return arrival.astype(np.int64)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
