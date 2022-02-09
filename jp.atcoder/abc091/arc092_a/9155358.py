import sys

n = int(sys.stdin.readline().rstrip())
abcd = list(zip(*[map(int, sys.stdin.read().split())] * 2))
ab = abcd[:n]
cd = abcd[n:]

def main():
    abcd.sort(key=lambda x: x[0])
    blue = list(map(lambda x: x[1], abcd))
    ab.sort(key=lambda x: x[0], reverse=True)
    reversed_b_sorted_by_a = list(map(lambda x: x[1], ab))

    cnt = 0
    for b in reversed_b_sorted_by_a:
        i = blue.index(b)
        if i == len(blue) - 1:
            blue.remove(b)
            continue
        cand = [x for x in blue[i+1:] if x > b]
        if not cand:
            blue.remove(b)
            continue
        blue.remove(b)
        blue.remove(min(cand))
        cnt += 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
