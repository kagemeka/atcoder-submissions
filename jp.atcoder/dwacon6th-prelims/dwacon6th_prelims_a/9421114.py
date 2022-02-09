import sys

n = int(sys.stdin.readline().rstrip())
s, t = [], []
for _ in range(n):
    si, ti = sys.stdin.readline().split()
    s.append(si); t.append(int(ti))
x = sys.stdin.readline().rstrip()

def main():
    cum_t = t[1:n] + [0]
    for i in range(n-1, 0, -1):
        cum_t[i-1] += cum_t[i]

    return cum_t[s.index(x)]

if __name__ == '__main__':
    ans = main()
    print(ans)
