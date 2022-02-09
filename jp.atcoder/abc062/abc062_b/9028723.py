import sys

h, w = map(int, sys.stdin.readline().split())
canvas = ['#' * (w + 2)] + ['#' + sys.stdin.readline().rstrip() + '#' for _ in range(h)] + ['#' * (w + 2)]

def main():
    return canvas

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
