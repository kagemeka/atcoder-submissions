import typing


def main() -> None:
    s = input()
    m = len(s)

    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    numbers_to_index = dict(zip(numbers, range(len(numbers))))

    marks = ["S", "H", "D", "C"]
    mark_to_index = dict(zip(marks, range(len(marks))))

    def parse_as_sequence(s: str) -> typing.List[typing.Tuple[int, int]]:
        a = []
        i = 0
        while i < m:
            mark = s[i]
            i += 1
            mark_index = mark_to_index[mark]
            if s[i : i + 1] in numbers_to_index:
                number_index = numbers_to_index[s[i : i + 1]]
                i += 1
            else:
                number_index = numbers_to_index[s[i : i + 2]]
                i += 2
            a.append((mark_index, number_index))
        return a

    a = parse_as_sequence(s)

    count = [0] * 4

    def in_target_range(number_index: int) -> bool:
        return number_index == 0 or number_index >= 9

    i = -1
    for mark_index, number_index in a:
        i += 1
        if in_target_range(number_index):
            count[mark_index] += 1
        if count[mark_index] == 5:
            target_index = mark_index
            break

    discarded_card_strings = []
    for mark_index, number_index in a[:i]:
        if mark_index == target_index and in_target_range(number_index):
            continue
        discarded_card_strings.append(marks[mark_index] + numbers[number_index])
    print(0 if not discarded_card_strings else ''.join(discarded_card_strings))


if __name__ == "__main__":
    main()
