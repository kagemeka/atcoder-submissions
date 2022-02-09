import sys
from collections import Counter

def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    c = Counter(s)
    res = (c.get('R', 0) & 1) + (c.get('G', 0) & 1) + (c.get('B', 0) & 1)
    '''
    4色以上だと絶対ではないが、3色以下ならうまくやると絶対に消せる。
    ので同じ色が２つ以上残ることはない
    なぜ消せるか。まず両サイドに２種類違う色があるとして、
    次の色がどちらかと同じであればそちらのサイドに入れて消せる。
    そうでない場合、次の次の色は三色のどれかなので次のボールを入れる側によっては必ず消せる。
    これを繰り返していくと、同じ色が２つ以上残ることは絶対にない。
    '''

    print(res)

if __name__ == '__main__':
    main()
