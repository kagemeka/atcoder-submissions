import typing


def compress_array(
    arr: typing.List[int],
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    """Compress array.

    return
        compressed_array
        retrieve_array
    """
    import bisect

    v = sorted(set(arr))
    return [bisect.bisect_left(v, x) for x in arr], v


def compute_inversion_number(arr: typing.List[int]) -> int:
    r"""Inversion Number of array.

    Args:
        arr (typing.List[int]): integer array.

    Returns:
        int: inversion number.

    Complexity:
        time: O(N\log{N})
        space: O(N)
        where:
            N: size of arr.
    """
    arr, _ = compress_array(arr)
    fw = FenwickTreeIntAdd([0] * len(arr))
    count = 0
    for i, x in enumerate(arr):
        count += i - fw[x]
        fw[x] = 1
    return count


class FenwickTreeIntAdd:
    """FenwickTreeIntAdd."""

    def __init__(self, arr: typing.List[int]) -> None:
        """Initialize.

        Args:
            arr (typing.List[int]): original array.
        """
        n = len(arr)
        data = [0] * (n + 1)
        data[1:] = arr.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n:
                continue
            data[j] += data[i]
        self.__data = data

    def __len__(self) -> int:
        """Length.

        Returns:
            int: length of original array.
        """
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: int) -> None:
        r"""Set.

        Args:
            i (int): index to add.
            x (int): value to add.

        Complexity:
            time: O(\log{N})
        """
        assert 0 <= i < len(self.__data) - 1
        i += 1
        while i < len(self.__data):
            self.__data[i] += x
            i += i & -i

    def __getitem__(self, i: int) -> int:
        """Get.

        Args:
            i (int): upper bound of sum [0, i)

        Returns:
            int: sum [0, i)
        """
        assert 0 <= i < len(self.__data)
        v = 0
        while i > 0:
            v += self.__data[i]
            i -= i & -i
        return v


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    cnt = compute_inversion_number(a)
    for x in a:
        print(cnt)
        cnt -= x
        cnt += n - 1 - x


if __name__ == "__main__":
    main()
