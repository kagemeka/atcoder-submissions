import sys

a, b = sys.stdin.readline().split()

def main():
    s = a * int(b)
    t = b * int(a)
    return s if s < t else t

if __name__ == '__main__':
    ans = main()
    print(ans)
