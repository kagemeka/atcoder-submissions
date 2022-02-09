import sys

# この問題におけるswapの意味を考えると、２つのものを　swapした場合に
# 左側が確定することから、一度swapされたcharacterが元のindexに戻ることはありえない。
# よって、changedとして一度でもswapされたindexを記録していけば良い

n, k = map(int, sys.stdin.readline().split())
s = [ord(c) - 97 for c in sys.stdin.readline().rstrip()]

def swap(i, j):
    s[i], s[j] = s[j], s[i]

def main():
    r = k
    changed = [False] * n

    for i in range(n-1):
        m = min(s[i+1:])
        if m < s[i]: # swapしたい
            for j in range(n-1, i, -1):
                if s[j] == m:
                    break
            c = changed[i] + changed[j]
            if c == 2:
                swap(i, j)
            elif c == 1:
                if r >= 1:
                    swap(i, j)
                    r -= 1
                    changed[i], changed[j] = True, True
            elif c == 0:
                if r >= 2:
                    swap(i, j)
                    r -= 2
                    changed[i], changed[j] = True, True

    ans = ''.join([chr(o + 97) for o in s])
    print(ans)

if __name__ == '__main__':
    main()
