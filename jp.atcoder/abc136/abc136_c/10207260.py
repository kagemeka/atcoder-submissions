import sys

n, *H = map(int, sys.stdin.read().split())

def main():
    cur = 0
    for h in H:
        if h > cur:
            cur = h - 1
        elif h < cur:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
