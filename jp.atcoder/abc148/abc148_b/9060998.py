import sys

n = int(sys.stdin.readline().rstrip())
s, t = sys.stdin.readline().split()

def main():
    res = [None] * n * 2
    res[::2] = list(s)
    res[1::2] = list(t)
    return ''.join(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
