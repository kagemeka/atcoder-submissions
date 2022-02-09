import sys
import math

def main():
    a, b, k = map(int, sys.stdin.readline().split())
    query_range = range(a, b + 1)
    print('aaa')
    exit()
    query_range = list(query_range)

    if a == b:
        res = query_range
    elif k >= math.ceil((b - a + 1) / 2):
        res = query_range
    else:
        res = query_range[:k] + query_range[-k:]

    for i in res:
        print(i)

if __name__ == "__main__":
    main()
