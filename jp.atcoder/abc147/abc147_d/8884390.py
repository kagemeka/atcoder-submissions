import sys
import numpy as np

MOD = 10 ** 9 + 7

N, *A = map(int, sys.stdin.read().split())
A = np.array(A, dtype=np.int64)

def main():
    answer = 0
    for n in range(60):
        B = (A >> n) & 1
        x = np.count_nonzero(B)
        y = N - x
        x *= y
        x *= pow(2, n, MOD)
        answer += x
    answer %= MOD
    return answer

if __name__ == '__main__':
    ans = main()
    print(ans)
