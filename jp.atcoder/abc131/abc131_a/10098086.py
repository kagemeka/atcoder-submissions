import sys

s = sys.stdin.readline().rstrip()

def main():
    for i in range(3):
        if s[i] == s[i+1]:
            return 'Bad'
    return 'Good'

if __name__ == '__main__':
    ans = main()
    print(ans)
