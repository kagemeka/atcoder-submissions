import sys

n = int(sys.stdin.readline().rstrip())
ab = map(int, sys.stdin.read().split())
ab = list(zip(ab, ab))

def main():
    c_a = ab[0][0]
    c_b = ab[0][1]
    for a, b in ab[1:]:
        ratio = a / b
        while c_a / c_b != ratio:
            if c_a / c_b < ratio:
                c_a += 1
            else:
                c_b += 1

    ans = c_a + c_b
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
