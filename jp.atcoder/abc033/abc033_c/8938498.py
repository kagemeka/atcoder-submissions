import sys
from string import digits

s = sys.stdin.readline().rstrip()

def main(s):
    for d in digits[2:]:
        s = s.replace(d, '1')
    ans = eval(s)
    return ans

if __name__ == '__main__':
    ans = main(s)
    print(ans)
