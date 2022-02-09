import sys

*T, = map(int ,sys.stdin.read().split())

def main():
    res = 0
    e = 10
    for t in T:
        res += 10 * ((t + 10 - 1) // 10)
        e = min(e, (t - 1) % 10 + 1)

    res -= (10 - e)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
