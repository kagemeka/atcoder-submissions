import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
    area1 = a * b
    area2 = c * d
    return area1 if area1 >= area2 else area2

if __name__ == '__main__':
    ans = main()
    print(ans)
