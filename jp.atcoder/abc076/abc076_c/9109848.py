import sys

s_prime, t = sys.stdin.read().split()
s = list(s_prime)
ls = len(s)
lt = len(t)

def main():
    ng = 'UNRESTORABLE'

    if ls < lt:
        return ng

    for i in range(ls-lt, -1, -1):
        t_prime = s[i:i+lt]
        for j in range(lt):
            letter = t_prime[j]
            if (letter != '?') and (letter != t[j]):
                break
        else:
            for j in range(lt):
                s[i+j] = t[j]
            break
    else:
        return ng

    ans = ''.join(s).replace('?', 'a')
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
