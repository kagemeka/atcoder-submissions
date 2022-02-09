import sys

h, w, = map(int, sys.stdin.readline().split())
canvas = sys.stdin.read().split()

def main():
    for i in range(h):
        for _ in range(2):
            yield canvas[i]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
