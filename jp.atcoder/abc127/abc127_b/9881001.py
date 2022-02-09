import sys

r, d, x_2000 = map(int, sys.stdin.readline().split())

def main():
    x = x_2000
    for _ in range(10):
        x = r*x - d
        yield x

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
