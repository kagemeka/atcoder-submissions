import sys

n, *b = map(int, sys.stdin.read().split())

def main():
    on = 1
    lightened = set([1])
    for i in range(1, n):
        on = b[on-1]
        if on == 2:
            return i
        if on in lightened:
            return -1
        lightened.add(on)

if __name__ == '__main__':
    ans = main()
    print(ans)
