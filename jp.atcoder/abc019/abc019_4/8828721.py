import sys

n = int(sys.stdin.readline().rstrip())

def ask(u, v):
    print('? {0} {1}'.format(u, v), flush=True)
    return int(sys.stdin.readline().rstrip())

def main():
    dist = 0
    for v in range(2, n + 1):
        d = ask(1, v)
        if d > dist:
            dist, u = d, v

    for v in range(2, n + 1):
        if v != u:
            dist = max(dist, ask(u, v))

    return '! {0}'.format(dist)

if __name__ == '__main__':
    ans = main()
    print(ans)
