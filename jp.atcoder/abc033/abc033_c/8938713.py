import sys
from string import digits

s = sys.stdin.readline().rstrip()

def main(s):
    for d in digits[2:]:
        s = s.replace(d, '1')
    ans = sum([eval(seq) for seq in s.split('+')])
    # 長過ぎて一度に評価できない
    return ans

if __name__ == '__main__':
    ans = main(s)
    print(ans)
