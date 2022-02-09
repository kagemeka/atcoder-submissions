import sys

s = sys.stdin.readline().rstrip()

def main():
    ans = 'Good'
    for i in range(3):
        if s[i] == s[i+1]:
            ans = 'Bad'
            break
    print(ans)

if __name__ ==  '__main__':
    main()
