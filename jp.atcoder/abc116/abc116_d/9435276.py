import sys
from heapq import heappush, heappop

n, k, *td = map(int, sys.stdin.read().split())
td = list(zip(*[iter(td)] * 2))

def main():
    td.sort(key=lambda x: x[1], reverse=True)
    delis = [[] for _ in range(n+1)]
    cnt = [0] * (n + 1)
    base = 0
    x = 0
    toppings = set()
    for t, d in td[:k]:
        toppings.add(t)
        if cnt[t] == 0:
            x += 1
        cnt[t] += 1
        heappush(delis[t], d)
        base += d
    score = base + x * x

    cand_to_remove = []
    for t in range(1, n+1):
        if cnt[t] >= 2:
            heappush(cand_to_remove, (heappop(delis[t]), t))
            cnt[t] -= 1

    for t, d in td[k:]:
        if not cand_to_remove:
            break
        if t in toppings:
            continue
        r_d, r_t = heappop(cand_to_remove)
        toppings.add(t)
        base -= r_d
        cnt[t] += 1
        heappush(delis[t], d)
        base += d
        x += 1
        if cnt[r_t] >= 2:
            heappush(cand_to_remove, (heappop(delis[r_t]), r_t))
            cnt[r_t] -= 1
        score = max(score, base + x * x)

    return score

if __name__ == '__main__':
    ans = main()
    print(ans)
