import sys

n, t, *a = map(int, sys.stdin.read().split())

def main():
    r = 0
    cnt = 0
    prof = 0
    max_prof = 0
    buy_price = sell_price = a[0]
    while True:
        r += 1
        if r == n:
            if prof == max_prof:
                cnt += 1
            elif prof > max_prof:
                max_prof = prof
                cnt = 1
            break

        cur = a[r]
        if cur > sell_price:
            sell_price = cur
            prof = sell_price - buy_price
        elif cur > buy_price:
            pass
        else:
            if prof == max_prof:
                cnt += 1
            elif prof > max_prof:
                max_prof = prof
                cnt = 1
            buy_price = sell_price = cur
            prof = 0

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
