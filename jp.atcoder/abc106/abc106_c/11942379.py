import sys

s, k = sys.stdin.read().split()
k = int(k)

def main():
    for i in range(min(k, len(s))):
        if s[i] != '1':
            print(s[i])
            return
    print(1)

if __name__ ==  '__main__':
    main()
