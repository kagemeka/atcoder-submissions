import sys

a, b = map(int, sys.stdin.readline().split())
if a > b:
    a, b = b, a

def main():
    d  = b - a
    if d <= 1:
        return 'Yay!'
    elif 16 - a * 2 >= d * 2:
        return 'yay!'
    else:
        return ':('

if __name__ == '__main__':
    ans = main()
    print(ans)
