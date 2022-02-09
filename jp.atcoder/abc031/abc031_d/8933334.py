import sys
from itertools import product

k, n = map(int, sys.stdin.readline().split())
v, w = [], []
for _ in range(n):
    vi, wi = sys.stdin.readline().split()
    v.append([int(x) - 1 for x in vi])
    w.append(wi)

def main():
    for lengths in list(product(range(1, 4), repeat=k)):
        for i in range(n):
            sum_len = 0
            for j in v[i]:
                sum_len += lengths[j]
            if sum_len != len(w[i]):
                break
        else:
            convert = [None] * k
            for i in range(n):
                cur = 0
                letters = w[i]
                for j in v[i]:
                    res = letters[cur:cur + lengths[j]]
                    if not convert[j]:
                        convert[j] = res
                    else:
                        if res != convert[j]:
                            break
                    cur += lengths[j]
                else:
                    continue
                break
            else:
                return convert

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
