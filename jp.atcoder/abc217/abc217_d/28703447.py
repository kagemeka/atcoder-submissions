from __future__ import annotations

import dataclasses
import typing

V = typing.TypeVar("V")


@dataclasses.dataclass
class Node(typing.Generic[V]):
    pivot: int
    key: int
    value: V
    left: typing.Optional[Node[V]] = None
    right: typing.Optional[Node[V]] = None
    size: int = 1


def _get_size(root: typing.Optional[Node[V]]) -> int:
    return 0 if root is None else root.size


def _update(root: Node[V]) -> None:
    root.size = _get_size(root.left) + _get_size(root.right) + 1


def new_tree_root(max_height: int, key: int, value: V) -> Node[V]:
    assert max_height >= 1
    assert 1 <= key < 1 << max_height
    return Node[V](1 << (max_height - 1), key, value)


def insert(root: Node[V], key: int, value: V) -> None:
    if key == root.key:
        raise Exception("you cannot insert the same key multiple times.")
    piv = root.pivot
    lsb = piv & -piv
    if not piv - (lsb - 1) <= key <= piv + (lsb - 1):
        raise Exception("the given key is out of bounds")
    if key < root.key:
        lo_key, lo_value = key, value
        hi_key, hi_value = root.key, root.value
    else:
        lo_key, lo_value = root.key, root.value
        hi_key, hi_value = key, value

    if lo_key < root.pivot:
        root.key, root.value = hi_key, hi_value
        if root.left is None:
            root.left = Node(piv - lsb // 2, lo_key, lo_value)
        else:
            insert(root.left, lo_key, lo_value)
    else:
        root.key, root.value = lo_key, lo_value
        if root.right is None:
            root.right = Node(piv + lsb // 2, hi_key, hi_value)
        else:
            insert(root.right, hi_key, hi_value)
    root.size += 1


def find(root: typing.Optional[Node[V]], key: int) -> typing.Optional[Node[V]]:
    if root is None:
        return None
    if key == root.key:
        return root
    elif key < root.key:
        return find(root.left, key)
    else:
        return find(root.right, key)


def _get_min(root: Node[V]) -> typing.Tuple[int, V]:
    if root.left is None:
        return (root.key, root.value)
    return _get_min(root.left)


def _get_max(root: Node[V]) -> typing.Tuple[int, V]:
    if root.right is None:
        return (root.key, root.value)
    return _get_max(root.right)


def remove(
    root: typing.Optional[Node[V]],
    key: int,
) -> typing.Optional[Node[V]]:
    if root is None:
        return None
    if key < root.key:
        root.left = remove(root.left, key)
    elif key > root.key:
        root.right = remove(root.right, key)
    else:
        if root.left is None and root.right is None:
            return None
        if root.right is not None:
            root.key, root.value = _get_min(root.right)
            root.right = remove(root.right, root.key)
        elif root.left is not None:
            root.key, root.value = _get_max(root.left)
            root.left = remove(root.left, root.key)
    _update(root)
    return root


def get_kth_node(root: Node[V], k: int) -> typing.Optional[Node[V]]:
    assert k >= 0
    i = _get_size(root.left)
    if k == i:
        return root
    if k < i:
        assert root.left is not None
        return get_kth_node(root.left, k)
    if root.right is None:
        return None
    return get_kth_node(root.right, k - i - 1)


def lower_bound(root: typing.Optional[Node[V]], key: int) -> int:
    if root is None:
        return 0
    if root.key < key:
        return _get_size(root.left) + 1 + lower_bound(root.right, key)
    return lower_bound(root.left, key)


def upper_bound(root: typing.Optional[Node[V]], key: int) -> int:
    if root is None:
        return 0
    if root.key <= key:
        return _get_size(root.left) + 1 + upper_bound(root.right, key)
    return upper_bound(root.left, key)


class PivotTreeSet:
    __root: typing.Optional[Node[None]]
    __max_height: int

    def __init__(self, max_height: int) -> None:
        self.__root = None
        self.__max_height = max_height

    @property
    def max_size(self) -> int:
        return (1 << self.__max_height) - 1

    def __len__(self) -> int:
        return 0 if self.__root is None else self.__root.size

    def __contains__(self, key: int) -> bool:
        assert 0 <= key < self.max_size
        return find(self.__root, key + 1) is not None

    def __getitem__(self, i: int) -> int:
        assert 0 <= i < len(self)
        assert self.__root is not None
        node = get_kth_node(self.__root, i)
        assert node is not None
        return node.key - 1

    def insert(self, key: int) -> None:
        assert 0 <= key < self.max_size
        if key in self:
            return
        key += 1
        if self.__root is None:
            self.__root = new_tree_root(self.__max_height, key, None)
        else:
            insert(self.__root, key, None)

    def remove(self, key: int) -> None:
        assert 0 <= key < self.max_size
        self.__root = remove(self.__root, key + 1)

    def lower_bound(self, key: int) -> int:
        return lower_bound(self.__root, key + 1)

    def upper_bound(self, key: int) -> int:
        return upper_bound(self.__root, key + 1)

    def min(self) -> typing.Optional[int]:
        return None if self.__root is None else self[0]

    def max(self) -> typing.Optional[int]:
        return None if self.__root is None else self[len(self) - 1]


def main() -> None:
    l_max, q = map(int, input().split())
    s = PivotTreeSet(30)
    s.insert(0)
    s.insert(l_max)
    res = []
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            s.insert(x)
            continue
        i = s.lower_bound(x)
        assert 1 <= i < len(s)
        res.append(s[i] - s[i - 1])
    print(*res, sep="\n")


main()
