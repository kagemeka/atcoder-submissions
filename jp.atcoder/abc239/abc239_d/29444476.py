def sieve_of_eratosthenes(sieve_size: int) -> list[bool]:
    assert sieve_size > 1
    is_prime = [True] * sieve_size
    is_prime[0] = is_prime[1] = False
    for i in range(2, sieve_size):
        if i * i >= sieve_size:
            break
        if not is_prime[i]:
            continue
        for j in range(i * i, sieve_size, i):
            is_prime[j] = False
    return is_prime


def main() -> None:
    a, b, c, d = map(int, input().split())

    is_prime = sieve_of_eratosthenes(1 << 8)

    for x in range(a, b + 1):
        for y in range(x + c, x + d + 1):
            if not is_prime[y]:
                continue
            else:
                break
        else:
            print("Takahashi")
            return
    print("Aoki")


main()
