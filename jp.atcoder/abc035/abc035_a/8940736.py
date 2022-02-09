import sys

w, h = map(int, sys.stdin.readline().split())

def main():
    if w / h == 16 / 9:
        return '16:9'
    return '4:3'

if __name__ == '__main__':
    ans = main()
    print(ans)
