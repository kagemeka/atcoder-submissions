import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    ans = (a*b + b*c + c*a) * 2
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
