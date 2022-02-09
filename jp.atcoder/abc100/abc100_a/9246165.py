import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    return 'Yay!' if a <= 8 and b <= 8 else ':('

if __name__ == '__main__':
    ans = main()
    print(ans)
