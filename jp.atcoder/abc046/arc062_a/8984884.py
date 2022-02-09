import sys

n = int(sys.stdin.readline().rstrip())
ab = map(int, sys.stdin.read().split())
ab = zip(ab, ab)

def main():
    c_a = c_b = 1
    for a, b in ab:
        t_a = (c_a + a - 1) // a
        t_b = (c_b + b - 1) // b
        t = max(t_a, t_b)
        c_a = a * t
        c_b = b * t

    ans = c_a + c_b
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
