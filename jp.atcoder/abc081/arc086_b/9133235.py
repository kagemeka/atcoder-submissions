import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    ma = 0
    idx = 0
    for i in range(n):
        cur = abs(a[i])
        if cur > ma:
            ma = cur
            idx = i

    if a[idx] == 0:
        print(0)
        sys.exit()

    procedures = []
    for i in range(n):
        a[i] += a[idx]
        procedures.append('{0} {1}'.format(idx+1, i+1))

    if a[idx] > 0:
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i+1] += a[i]
                procedures.append('{0} {1}'.format(i+1, i+2))
    else:
        for i in range(n-1, 0, -1):
            if a[i] < a[i-1]:
                a[i-1] += a[i]
                procedures.append('{0} {1}'.format(i+1, i))

    procedures = [len(procedures)] + procedures
    return procedures

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
