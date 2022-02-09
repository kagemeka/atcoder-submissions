import sys

s, t = sys.stdin.read().split()
n = len(s); m = len(t)
s = list(s)

def main():
    for i in range(n - m, -1, -1):
        for j in range(m):
            if t[j] != s[i+j] != '?':
                break
        else:
            for j in range(m):
                s[i+j] = t[j]
            for i in range(n):
                if s[i] == '?': s[i] = 'a'
            print(''.join(s))
            return
    print('UNRESTORABLE')

if __name__ ==  '__main__':
    main()
