import sys

n = int(sys.stdin.readline().rstrip())

def main():
    if n < 60: ans = 'Bad'
    elif n < 90: ans = 'Good'
    elif n < 100: ans = 'Great'
    else: ans = 'Perfect'
    print(ans)

if __name__ ==  '__main__':
    main()
