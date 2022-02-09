import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    for i in range(1, 1251):
        if i * 0.1 // 1 == b and i * 0.08 // 1 == a:
            return i
    return -1

if __name__ == '__main__':
    ans = main()
    print(ans)
