import sys
from itertools import product

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
resp = s
resp = resp.replace('o', '1')
resp = resp.replace('x', '0')
resp = [None] + [int(x) for x in resp]

def restore(pattern):
    for i in range(1, n):
        if resp[i] ^ pattern[i]:
            pattern[i+1] = 1 if pattern[i-1] ^ 1 else 0
        else:
            pattern[i+1] = pattern[i-1]
    return pattern

def contradicting(pattern):
    if pattern[0] != pattern[-1]:
        return True
    if resp[-1] ^ pattern[-1]:
        if not pattern[-2] ^ pattern[1]:
            return True
    else:
        if pattern[-2] ^ pattern[1]:
            return True
    return False

def main():
    res = [None] * (n + 1)
    for i in range(4):
        pattern = res.copy()
        pattern[0] = i >> 0 & 1
        pattern[1] = i >> 1 & 1
        ans = restore(pattern)
        if not contradicting(ans):
            t = ''
            for i in range(1, n+1):
                t += 'S' if ans[i] & 1 else 'W'
            return t
    return -1

if __name__ == '__main__':
    ans = main()
    print(ans)
