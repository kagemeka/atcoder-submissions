import sys

x, y = sys.stdin.readline().split()

def main():
    if x > y:
        return '>'
    elif x < y:
        return '<'
    else:
        return '='

if __name__ == '__main__':
    ans = main()
    print(ans)
