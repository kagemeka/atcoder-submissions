import sys

a = int(sys.stdin.readline().rstrip())

def main():
    if a & 1:
        return a // 2 * (a // 2 + 1)
    return (a // 2) ** 2

if __name__ == '__main__':
    ans = main()
    print(ans)
