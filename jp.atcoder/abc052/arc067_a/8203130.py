def primeFactorize(n):
    if n > 1:
        prime_factors = []
        while n % 2 == 0:
            n //= 2
            # n is divisible by 2 so 'n //= 2' is equal to
            # 'n /= 2'. but '//=' returns an integer, whereas
            # '/=' returns a float.
            prime_factors.append(2)

        # n cannot be a even number at this point.
        # so range is from 3 to int(n**0.5), but step is 2.
        for i in range(3, int(n**0.5)+1, 2):
            while n % i == 0:
                n //= i
                prime_factors.append(i)
            if n == 1: # otherwise, n > i.
                return prime_factors
        # if n != 1, n > i(int(n**0.5) or int(n**0.5)-1).
        # (i == int(n**0.5) if int(n**0.5) is an odd number.)
        # (i == int(n**0.5)-1 if int(n**0.5) is an even number.)
        prime_factors.append(n)
        return prime_factors
    else:
        return []


def findPrimeNumbers(n):
    # return a list of prime numbers less than or equal to n.
    prime_numbers = [2]
    for i in range(3, n+1, 2):

        for j in prime_numbers:
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)

    return prime_numbers

mod = 10 ** 9 + 7
N = int(input())

prime_factors_of_the_factorial_of_n = []
for i in range(1, N+1):
    prime_factors_of_the_factorial_of_n += primeFactorize(i)

count_of_each_prime_number = []
for i in findPrimeNumbers(N):
    count_of_each_prime_number.append(
        prime_factors_of_the_factorial_of_n.count(i)
    )


ans = 1
for c in count_of_each_prime_number:
    ans *= c + 1

print(ans % mod)
