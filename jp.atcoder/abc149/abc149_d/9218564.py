import sys

n, k = map(int, sys.stdin.readline().split())
r, s, p = map(int, sys.stdin.readline().split())
t = sys.stdin.readline().rstrip()
point = dict([('r', r), ('s', s), ('p', p)])

def hand(opponent):
    if opponent == 'r':
        return 'p'
    elif opponent == 's':
        return 'r'
    elif opponent == 'p':
        return 's'

def main():
    res = 0
    for i in range(k):
        cur = hand(t[i])
        res += point[cur]
        prev = cur
        for j in range(i+k, n, k):
            cur = hand(t[j])
            if cur == prev:
                cur = t[j]
            else:
                res += point[cur]
            prev = cur
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
