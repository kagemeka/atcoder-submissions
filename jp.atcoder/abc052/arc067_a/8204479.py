import math
mod = int(1e9+7)

N = int(input())
n = math.factorial(N)

count_of_prime_factors = {}
while True:
    if n > 1:
        count = 0
        while n % 2 == 0:
            n //= 2
            count += 1
        if count != 0:
            count_of_prime_factors.update({2: count})
        if n == 1:
            break

        for i in range(3, N+1, 2):
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count != 0:
                count_of_prime_factors.update({i: count})
            if n == 1:
                break
        else:
            count_of_prime_factors.update({n: 1})
        break
    else:
        print(1)
        exit()

ans = 1
for prime_factor, count in count_of_prime_factors.items():
    ans *= count + 1

print(ans % mod)
print(count_of_prime_factors)
