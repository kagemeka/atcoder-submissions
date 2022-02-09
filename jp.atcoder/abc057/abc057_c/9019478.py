import sys

n = int(sys.stdin.readline().rstrip())

def main():
    a = 1
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a = i
    b = n // a
    ans = len(str(b))
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
