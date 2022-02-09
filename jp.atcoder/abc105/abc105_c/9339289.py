import sys

n = int(sys.stdin.readline().rstrip())

def to_neg_base(n, neg_base):
    if neg_base > -2:
        sys.exit('base must be at most -2')
    b = abs(neg_base)
    res = [0] * 100
    if n >= 0:
        res[0] = n
        i = 0
    else:
        q, r = divmod(n, b)
        res[0] = r; res[1] = abs(q)
        i = 1

    while res[i] >= b:
        q, r = divmod(res[i], b)
        m = min(q, res[i+1])
        q -= m
        res[i+1] -= m
        res[i] = r
        res[i+1] += (b - 1) * q
        res[i+2] += q
        i += 1

    res = ''.join(list(map(str, res)))[::-1]
    try:
        return int(res[res.index('1'):])
    except:
        return 0

def main():
    return to_neg_base(n, -2)

if __name__ == '__main__':
    ans = main()
    print(ans)
