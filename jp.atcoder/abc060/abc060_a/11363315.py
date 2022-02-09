import sys

s = sys.stdin.readline().split()

def main():
    ans = 'YES'
    for i in range(2):
        if s[i][-1] != s[i+1][0]:
            ans = 'NO'
            break
    print(ans)

if __name__ ==  '__main__':
    main()
