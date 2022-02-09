import sys

x, y = map(int, sys.stdin.readline().split())

def main():
    return  'Brown' if abs(x - y) <= 1 else 'Alice'

if __name__ == '__main__':
    ans = main()
    print(ans)
