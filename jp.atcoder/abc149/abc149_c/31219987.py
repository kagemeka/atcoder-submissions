def main() -> None:
    def is_prime(n: int) -> bool:
        for i in range(2, n):
            if i * i > n:
                break
            if n % i == 0:
                return False
        return True

    x = int(input())
    while not is_prime(x):
        x += 1
    print(x)


if __name__ == "__main__":
    main()
