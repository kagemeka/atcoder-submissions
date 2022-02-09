import sys

a, p = map(int, sys.stdin.readline().split())

def main():
    return (3 * a + p) // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
