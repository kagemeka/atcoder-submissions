import sys

k = int(sys.stdin.readline().rstrip())

def main():
    return (k - k // 2) * (k // 2)

if __name__ == '__main__':
    ans = main()
    print(ans)
