import sys

s, k = sys.stdin.read().split()
k = int(k)

def main():
    cand = set()
    for j in range(1, k + 1):
        for i in range(len(s) - j + 1):
            cand.add(s[i:i+j])
    print(sorted(cand)[k-1])

if __name__ ==  '__main__':
    main()
