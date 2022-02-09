import sys

s = sys.stdin.readline().rstrip()

def main():
    l = len(s)
    t = s[:-1] if l & 1 else s
    l = len(t)
    while True:
        t = t[:-2]
        l -= 2
        if t[:l//2] * 2 == t:
            return l

if __name__ == '__main__':
    ans = main()
    print(ans)
