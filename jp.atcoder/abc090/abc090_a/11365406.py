import sys

s = sys.stdin.read().split()

def main():
    t = ''
    for i in range(3): t += s[i][i]
    print(t)

if __name__ ==  '__main__':
    main()
