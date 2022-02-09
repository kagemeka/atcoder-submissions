import math
mod = int(1e9+7)

N = int(input())

factorial_of_n = math.factorial(N)

def countOfPrimeFactors(n):
    # when n > factorial(196), system may overflows
    # if then, try to replace 'int(n**0.5)+1' by 'n'
    count_of_prime_factors = {}
    if n > 1:
        count = 0
        while n % 2 == 0:
            n //= 2
            count += 1
        if count != 0:
            count_of_prime_factors.update({2: count})
        if n == 1:
            return count_of_prime_factors

        for i in range(3, n, 2):
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            if count != 0:
                count_of_prime_factors.update({i: count})
            if n == 1:
                return count_of_prime_factors

        count_of_prime_factors.update({n: 1})
        return count_of_prime_factors
    else:
        return {}

ans = 1
for prime_factor, count in countOfPrimeFactors(factorial_of_n).items():
    ans *= count + 1

print(ans % mod)
