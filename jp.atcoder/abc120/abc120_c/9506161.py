import sys

s = sys.stdin.readline().rstrip()

def main():
    return min(s.count('0'), s.count('1')) * 2

if __name__ == '__main__':
    ans = main()
    print(ans)
