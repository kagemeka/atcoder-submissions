# 2019-11-23 21:00:35(JST)
import sys
import itertools

def main():
    n, *A = map(int, sys.stdin.read().split())

    S = sum(A)
    l = 0
    for i in range(n):
        l += A[i]
        if l >= S // 2:
            if l == S / 2:
                ans = 0
                break
            else:
                if l == S // 2 - 1:
                    ans = 1
                    break
                else:
                    if l - A[i] >= S - l:
                        ans = A[i] + (S - l) - (l - A[i])
                    else:
                        ans = l - (S - l)
                    break

    print(ans)





if __name__ == '__main__':
    main()
