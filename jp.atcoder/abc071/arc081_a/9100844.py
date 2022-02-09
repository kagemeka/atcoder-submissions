import sys

n, *l = map(int, sys.stdin.read().split())

def main():
    l.sort(reverse=True)

    a = b = 0
    i = 0
    while i <= n - 2:
        if l[i] == l[i+1]:
            if a:
                b = l[i]
                break
            else:
                a = l[i]
                i += 2
                continue
        i += 1

    return a * b

if __name__ == '__main__':
    ans = main()
    print(ans)
