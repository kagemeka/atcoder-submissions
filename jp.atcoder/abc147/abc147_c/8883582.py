import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
xy = [[] for _ in range(n)]
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    for _ in range(a):
        x, y = map(int, sys.stdin.readline().split())
        xy[i].append((x - 1, y))

def main():
    comb = (np.arange(2 ** n).reshape(-1, 1) >> np.arange(n) & 1).astype(np.bool)
    for i in range(n):
        for x, y in xy[i]:
            bl = ~comb[:, i] | (comb[:, x] == np.bool(y))
            comb = comb[bl] # ありえる組み合わせだけを残す
    '''
    ~comb[:, i]:= (i番目がUnkindと仮定したとき、)i番目をUnkind(False)としている組み合わせを残す
    (comb[:, x] == np.bool(y)):= (i番目がHonestと仮定したとき、)i番目の証言が矛盾しない組み合わせを残す
    '''

    ans = np.amax(np.sum(comb, axis=1))
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
