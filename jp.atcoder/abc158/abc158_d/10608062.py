import sys
from collections import deque

s = sys.stdin.readline().rstrip()
Q = int(sys.stdin.readline().rstrip())
Q = [sys.stdin.readline().split() for _ in range(Q)]

def main():
    res = deque(s)
    flag = 0
    cnt = 0
    for q in Q:
        if q[0] == '1':
            flag ^= 1
            cnt += 1
        else:
            f, c = q[1:]
            f = int(f) - 1
            if flag ^ f:
                res.append(c)
            else:
                res.appendleft(c)

    res = ''.join(list(res))
    if cnt & 1:
        res = res[::-1]
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
