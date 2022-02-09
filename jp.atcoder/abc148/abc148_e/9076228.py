import sys

n = int(sys.stdin.readline().rstrip())

def main():
    if n & 1:
        return 0
    ans = 0
    for i in range(30):
        ans += n // (10 * 5 ** i)

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
