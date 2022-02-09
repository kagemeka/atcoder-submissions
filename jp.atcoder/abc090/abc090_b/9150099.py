import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r

a, b = map(int, sys.stdin.readline().split())

def main():
    palindromic_nums = []
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                x = [i, j, k, j, i]
                palindromic_nums.append(int(''.join(list(map(str, x)))))

    return bi_r(palindromic_nums, b) - bi_l(palindromic_nums, a)

if __name__ == '__main__':
    ans = main()
    print(ans)
