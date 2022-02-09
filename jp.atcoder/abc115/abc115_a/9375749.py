import sys

d = int(sys.stdin.readline().rstrip())

def main():
    return 'Christmas' + ' Eve' * (25 - d)

if __name__ == '__main__':
    ans = main()
    print(ans)
