import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a = np.array(sys.stdin.read().split(), dtype=np.int64)

def main():
    mul_4 = n - np.count_nonzero(a % 4)
    mul_2 = n - np.count_nonzero(a % 2)

    if mul_4 >= n // 2:
        return 'Yes'
    if mul_4 * 2 + (mul_2 - mul_4) >= n:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
