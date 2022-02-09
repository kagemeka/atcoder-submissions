import typing


def is_palindrome(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True


def main() -> None:
    s = input()
    print("Yes" if is_palindrome(s.rstrip("a")) else "No")


if __name__ == "__main__":
    main()
