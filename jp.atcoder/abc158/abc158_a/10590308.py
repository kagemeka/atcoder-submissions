import sys

s = sys.stdin.readline().rstrip()

def main():
    return 'Yes' if len(set(s)) == 2 else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
