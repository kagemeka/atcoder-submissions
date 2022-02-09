import sys

s, k = sys.stdin.read().split()
k = int(k)

def main():
    res = set()
    for i in range(len(s) - k + 1):
        res.add(s[i:i+k])
    return len(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
