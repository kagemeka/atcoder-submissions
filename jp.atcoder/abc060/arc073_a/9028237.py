import sys

n, T, *t = map(int, sys.stdin.read().split())

def main():
    start = 0
    will_stop = T
    running_time = 0
    for i in range(1, n):
        cur = t[i]
        if cur < will_stop:
            running_time += cur - start
        else:
            running_time += T
        start = cur
        will_stop = cur + T
    running_time += T

    return running_time

if __name__ == '__main__':
    ans = main()
    print(ans)
