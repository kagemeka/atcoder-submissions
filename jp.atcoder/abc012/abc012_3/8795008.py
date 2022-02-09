import sys

n = int(sys.stdin.readline().rstrip())

def main():
    S = 45 ** 2
    r = S - n
    res = []
    for i in range(1, 10):
        if r % i == 0:
            j = r // i
            if j < 10:
                res.append('{0} x {1}'.format(i, j))
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
