import sys

s = sys.stdin.readline().split()

def main():
    res = ''
    for w in s:
        res += w[0]

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
