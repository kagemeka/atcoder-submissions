import sys

n, *ab = map(int, sys.stdin.read().split())
ab = sorted(zip(*[iter(ab)] * 2), key=lambda x: x[1])

def main():
    t = 0
    for a, b in ab:
        t += a
        if t > b:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
