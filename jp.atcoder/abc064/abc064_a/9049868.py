import sys

r, g, b = sys.stdin.readline().split()

def main():
    return 'NO' if int(g + b) % 4 else 'YES'

if __name__ == '__main__':
    ans = main()
    print(ans)
