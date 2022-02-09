import sys

n = int(sys.stdin.readline().rstrip())

def main():
    ans = 800 * n - 200 * (n // 15)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
