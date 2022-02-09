import sys

s = sys.stdin.readline().rstrip()

def main():
    ans = len(s) // 2 - s.count('p')
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
