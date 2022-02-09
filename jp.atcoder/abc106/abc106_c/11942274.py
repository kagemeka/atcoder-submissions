import sys

s, k = sys.stdin.read().split()
k = int(k)

def main():
    for i in range(len(s)):
        if s[i] != '1':
            print(1 if k < i + 1 else s[i])
            return

if __name__ ==  '__main__':
    main()
