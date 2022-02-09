import sys

strings = sys.stdin.readline().split()

def main():
    t = ''
    for s in strings:
        t += s[0].upper()
    return t

if __name__ == '__main__':
    ans = main()
    print(ans)
