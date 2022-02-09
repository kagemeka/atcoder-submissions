import sys

s = sys.stdin.readline().rstrip()

def main():
    if s[-1] == 'T':
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
