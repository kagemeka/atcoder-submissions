import sys

s = sys.stdin.readline().rstrip()

def main():
    l = len(s)
    if l & 1:
        return 'No'
    if s == 'hi' * (l // 2):
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
