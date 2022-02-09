import sys

n = int(sys.stdin.readline().rstrip())
table = {}
for _ in range(n):
    b, a = sys.stdin.readline().split()
    table[b] = a

n, *s = sys.stdin.read().split()

def main():
    t = ''
    for c in s:
        if c in table:
            t += table[c]
        else:
            t += c
    return t

if __name__ == "__main__":
    ans = main()
    print(ans)
