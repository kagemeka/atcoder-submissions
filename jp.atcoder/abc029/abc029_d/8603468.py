# 2019-11-24 16:35:46(JST)
import sys
# import numpy as np
# import itertools

def main():
    n = int(sys.stdin.readline().rstrip())


    count = 0
    for i in range(1, len(str(n))+1):
        q = (n+1) // 10 ** i
        r = (n+1) % 10 ** i
        count += q * 10 ** (i - 1)
        if r <= 10 ** (i - 1):
            pass
        elif r <= 10 ** (i - 1) * 2:
            count += r - 10 ** (i - 1)
        else:
            count += 10 ** (i - 1)


    print(count)

# editorial
if __name__ == '__main__':
    main()
