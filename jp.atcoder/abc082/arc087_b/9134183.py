import sys


s = sys.stdin.readline().rstrip()
x, y = map(int, sys.stdin.readline().split())

def reachable(deltas, goal):
    if not deltas:
        if goal == 0:
            return True
        else:
            return False

    s = sum(deltas)
    if goal < -s or s < goal:
        return False

    if (s - goal) & 1:
        return False

    a = (s - goal) // 2

    res = [False] * (a + 1)
    res[0] = True
    for d in deltas:
        for i in range(a+1):
            if res[i] and i + d <= a:
                res[i+d] = True
    return res[a]

def main():
    gx = x; gy = y
    dx = []
    dy = []
    direction = 0

    origin_x = 0
    for i in s:
        if i == 'T':
            break
        origin_x += 1
    gx -= origin_x

    tmp = 0
    for i in s[origin_x:] + 'T':
        if i == 'T':
            if direction == 0:
                if tmp != 0:
                    dx.append(tmp)
                direction = 1
            else:
                if tmp != 0:
                    dy.append(tmp)
                direction = 0
            tmp = 0
        else:
            tmp += 1

    return 'Yes' if reachable(dx, gx) & reachable(dy, gy) else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
