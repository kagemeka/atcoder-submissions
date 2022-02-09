import sys

n = sys.stdin.readline().rstrip()

def main():
    return 'Yes' if int(n) % sum([int(d) for d in n]) == 0 else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
