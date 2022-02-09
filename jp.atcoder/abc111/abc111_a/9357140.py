import sys

n = sys.stdin.readline().rstrip()

def main():
    res = n.replace('9', '0')
    res = res.replace('1', '9')
    res = res.replace('0', '1')
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
