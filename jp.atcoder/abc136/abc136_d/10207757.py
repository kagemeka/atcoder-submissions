import sys

s = sys.stdin.readline().rstrip()
n = len(s)
s += 'R'

def main():
    l = []
    for i in range(1, n):
        if s[i] == 'L':
            if s[i-1] == 'R':
                ls = i
            if s[i+1] == 'R':
                lg = i
                l.append((ls, lg))

    res = [0] * n
    j = 0
    ls, lg = l[j]
    for i in range(n):
        if i > lg:
            j += 1
            ls, lg = l[j]
        d = abs(ls - i)
        if d & 1:
            res[ls-1] += 1
        else:
            res[ls] += 1

    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
