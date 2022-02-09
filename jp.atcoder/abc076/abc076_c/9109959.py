import sys

s_prime, t = sys.stdin.read().split()
ls = len(s_prime)
lt = len(t)

def main():
    for i in range(ls-lt, -1, -1):
        t_prime = s_prime[i:i+lt]
        for j in range(lt):
            if not t_prime[j] in ['?', t[j]]:
                break
        else:
            s = (s_prime[:i] + t + s_prime[i+lt:]).replace('?', 'a')
            return s
    return 'UNRESTORABLE'

if __name__ == '__main__':
    ans = main()
    print(ans)
