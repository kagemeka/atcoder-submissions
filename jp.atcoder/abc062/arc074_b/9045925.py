import sys
from heapq import *

n, *a = map(int, sys.stdin.read().split())

def optimize(arr):
    res = arr[:n]
    heapify(res)
    sum_arr = [sum(res)]
    for x in arr[n:]:
        y = heappop(res)
        heappush(res, max(x, y))
        sum_arr.append(sum_arr[-1] + max(0, x - y))
    return sum_arr

def main():
    left = a[:n*2]
    right = [-x for x in a[n:]][::-1]

    sum_left = optimize(left)
    sum_right = optimize(right)

    res = []
    for i in range(n+1):
        res.append(sum_left[i] + sum_right[n-i])

    ans = max(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
