import sys

n = int(sys.stdin.readline().rstrip())
csf = list(zip(*[map(int, sys.stdin.read().split())] * 3))

def main():
    take_time = [None] * n

    for i in range(n):
        cur = i
        t = 0
        while cur < n - 1:
            c, s, f = csf[cur]
            if t < s:
                t = s
            else:
                t = s + f * ((t - s + f - 1) // f)
            t += c
            cur += 1
        take_time[i] = t
    return take_time

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
