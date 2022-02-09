import sys

n = int(sys.stdin.readline().rstrip())

def main():
    if n & 1:
        return n + 1
    return n - 1

if __name__ == '__main__':
    ans = main()
    print(ans)
