import sys
import numpy as np

def main():
    txa, tya, txb, tyb, T, V = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().rstrip())

    xy = np.array(sys.stdin.read().split(), dtype=np.float64).reshape(-1, 2)
    # reshape(-1, 2) とすると、行数が要素数を列数で割った数になる。reshape(2, -1)などもまた然り。

    x, y = xy.T # Transpose

    dist_a_to_girl = ((x - txa)**2 + (y - tya)**2) ** .5
    dist_girl_to_b = ((txb - x)**2 + (tyb - y)**2) ** .5

    if (dist_a_to_girl + dist_girl_to_b <= V * T).any(): # (boolean array).any()
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()
