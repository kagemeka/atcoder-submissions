import itertools
import typing


def main() -> None:
    N = 3
    strings = [input() for _ in range(N)]
    characters = set()
    for s in strings:
        characters |= set(s)

    UNSOLVABLE = "UNSOLVABLE"
    characters = tuple(characters)
    n = len(characters)
    if n > 10:
        print(UNSOLVABLE)
        return

    to_index = dict(zip(characters, range(n)))

    string_indices = [[to_index[c] for c in s] for s in strings]

    def is_ok(replaced: typing.List[typing.List[int]]) -> bool:
        for number in replaced:
            if number[0] == 0:
                return False

        numbers = [int("".join(map(str, number))) for number in replaced]
        return numbers[0] + numbers[1] == numbers[2]

    def replace_with(digits: typing.Tuple[int, ...]) -> typing.List[typing.List[int]]:
        return [[digits[i] for i in indices] for indices in string_indices]

    for digits in itertools.permutations(range(10), n):
        replaced = replace_with(digits)
        if not is_ok(replaced):
            continue

        for row in replaced:
            print("".join(map(str, row)))
        return

    print(UNSOLVABLE)


if __name__ == "__main__":
    main()
