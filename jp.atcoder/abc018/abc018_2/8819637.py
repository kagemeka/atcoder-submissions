import sys

s, n, *lr = sys.stdin.read().split()
lr = map(int, lr)
lr = zip(lr, lr)

def main():
    t = ' ' + s
    for l, r in lr:
        t = t[:l] + t[r:l-1:-1] + t[r+1:]

    return t.lstrip()

if __name__ == '__main__':
    ans = main()
    print(ans)
