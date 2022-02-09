import sys

s, k = sys.stdin.read().split()
k = int(k)
n = len(s)

def main():
    for i in range(1, n+1):
        if s[i-1] != '1':
            break

    return 1 if k < i else int(s[i-1])

if __name__ == '__main__':
    ans = main()
    print(ans)
