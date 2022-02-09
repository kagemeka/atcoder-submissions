import sys

s = sys.stdin.readline().rstrip()

def main():
    s1 = s[::2]
    s2 = s[1::2]
    res1 = s1.count('1') + s2.count('0')
    res2 = s1.count('0') + s2.count('1')
    return min(res1, res2)

if __name__ == '__main__':
    ans = main()
    print(ans)
