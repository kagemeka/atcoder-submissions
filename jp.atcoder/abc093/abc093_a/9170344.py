import sys

s = sys.stdin.readline().rstrip()

def main():
    return 'Yes' if ''.join(sorted(s)) == 'abc' else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
