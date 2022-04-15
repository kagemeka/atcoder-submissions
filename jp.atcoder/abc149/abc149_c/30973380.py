def main() -> None:
    x = int(input())

    def is_prime(x: int) -> bool:
        for i in range(2, x + 1):
            if i * i > x:
                return True
            if x % i == 0:
                return False

    while True:
        if is_prime(x):
            print(x)
            return
        x += 1


if __name__ == "__main__":
    main()
