import typing


def is_palindrome(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True


def main() -> None:
    s = input()
    left = 0
    right = 0
    n = len(s)
    for i in range(n):
        if s[i] == "a":
            left += 1
        else:
            break
    for i in range(n):
        if s[n - 1 - i] == "a":
            right += 1
        else:
            break
    # print(left, right)

    if left > right:
        print("No")
        return

    s = s[: n - (right - left)]
    # print(s)
    print("Yes" if is_palindrome(s) else "No")


if __name__ == "__main__":
    main()
