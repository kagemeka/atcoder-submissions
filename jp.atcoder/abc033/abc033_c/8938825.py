import sys
from string import digits

s = sys.stdin.readline().rstrip()

def main(s):
    for d in digits[2:]:
        s = s.replace(d, '1')

    # 長すぎるため eval()だとerror
    s = s.replace('*1', '')
    s = s.replace('1*0', '0')
    s = s.replace('*0', '')
    ans = s.count('1')
    return ans

if __name__ == '__main__':
    ans = main(s)
    print(ans)
