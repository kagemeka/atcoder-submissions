import sys
import numpy as np

# sum of deliciousness が border以上の組み合わせが K個以上あればTrue
def is_ok(a, b, c, X, Y, Z, K, border):
    cnt = 0
    for i in range(X):
        for j in range(Y):
            for k in range(Z):
                if a[i] + b[j] + c[k] < border:
                    break
                cnt += 1
                if cnt >= K:
                    return True
    return False

def main():
    x, y, z, K = map(int, sys.stdin.readline().split())
    abc = np.array(sys.stdin.read().split(), dtype=np.int64)
    a = abc[:x]
    b = abc[x:x + y]
    c = abc[x + y:x + y+ z]
    a = np.sort(a)[::-1]
    b = np.sort(b)[::-1]
    c = np.sort(c)[::-1]

    l, r = 3, 3 * 10 ** 10
    while l <= r:
        border = (l + r) // 2
        if is_ok(a, b, c, x, y, z, K, border):
            l = border + 1
        else:
            r = border - 1

    res = []
    cnt = 0
    for i in range(x):
        for j in range(y):
            for k in range(z):
                sum_deli = a[i] + b[j] + c[k]
                if sum_deli < r:
                    break
                res.append(sum_deli)
                cnt += 1
                if cnt >= K:
                    break


    res = sorted(res, reverse=True)[:K]
    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    main()
