import sys

n = int(''.join(sys.stdin.readline().split()))

def main():
    return 'Yes' if (n ** 0.5 // 1) ** 2 == n else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
