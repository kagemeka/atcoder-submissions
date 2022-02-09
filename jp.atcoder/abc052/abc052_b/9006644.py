import sys

n, s = sys.stdin.read().split()
n = int(n)

def main():
    t = s
    t = t.replace('I', '+')
    t = t.replace('D', '-')
    x = 0
    res = 0
    for i in range(n):
        x += eval(t[i] + '1')
        res = max(res, x)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
