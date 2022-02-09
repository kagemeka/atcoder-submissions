import sys

def o(c): return ord(c) - ord('a')

s, t = sys.stdin.read().split()

def main():
    g1 = [set() for _ in range(26)]
    g2 = [set() for _ in range(26)]
    for i in range(len(s)):
        a = o(s[i]); b = o(t[i])
        g1[a].add(b); g2[b].add(a)

    for i in range(26):
        if len(g1[i]) >= 2 or len(g2[i]) >= 2:
            print('No')
            return
    print('Yes')

if __name__ ==  '__main__':
    main()
