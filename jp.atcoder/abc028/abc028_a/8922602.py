import sys

n = int(sys.stdin.readline().rstrip())

def main():
    if n < 60:
        return 'Bad'
    elif n < 90:
        return 'Good'
    else:
        return 'Perfect'

if __name__ == '__main__':
    ans = main()
    print(ans)
