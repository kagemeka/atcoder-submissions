import sys

n, *A = map(int, sys.stdin.read().split())

def main():
    res = set(range(1, n+1)) - set(A)
    if not res:
        return 'Correct'
    b = res.pop()
    occured = set()
    for a in A:
        if a in occured:
            return '{0} {1}'.format(a, b)
        occured.add(a)

if __name__ == "__main__":
    ans = main()
    print(ans)
