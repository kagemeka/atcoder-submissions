import sys

s = sys.stdin.read().split()

def main():
    t = ''
    for i in range(3):
        t += s[i][i]
    return t

if __name__ == '__main__':
    ans = main()
    print(ans)
