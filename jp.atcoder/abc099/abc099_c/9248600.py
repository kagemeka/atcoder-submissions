import sys

n = int(sys.stdin.readline().rstrip())

def main():
    bit6 = [0] * 8
    bit9 = [0] * 7
    b = n
    for i in range(5, -1, -1):
        q, r = divmod(b, 9 ** i)
        bit9[i] = q
        b = r

    res = sum(bit6) + sum(bit9)

    for _ in range(n):
        i = 0
        while True:
            bit6[i] += 1
            if bit6[i] == 6:
                bit6[i] = 0
                i += 1
            else:
                break

        i = 0
        while True:
            bit9[i] -= 1
            if bit9[i] == -1:
                bit9[i] = 8
                i += 1
            else:
                break

        res = min(res, sum(bit6) + sum(bit9))

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
