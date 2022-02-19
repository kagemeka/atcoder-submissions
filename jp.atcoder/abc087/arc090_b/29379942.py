from __future__ import annotations

import dataclasses
import typing

T = typing.TypeVar("T")


@dataclasses.dataclass
class Monoid(typing.Generic[T]):
    identity: typing.Callable[[], T]
    operation: typing.Callable[[T, T], T]


@dataclasses.dataclass
class Group(Monoid[T]):
    invert: typing.Callable[[T], T]


class PotentialUnionFind(typing.Generic[T]):
    def __init__(self, group: Group[T], size: int) -> None:
        self.__group = group  # abelian group
        self.__data = [-1] * size
        self.__delta = [group.identity() for _ in range(size)]

    def __len__(self) -> int:
        return len(self.__data)

    def find_root(self, node: int) -> int:
        assert 0 <= node < len(self)
        if self.__data[node] < 0:
            return node
        parent = self.__data[node]
        root = self.find_root(parent)
        self.__delta[node] = self.__group.operation(
            self.__delta[node],
            self.__delta[parent],
        )
        self.__data[node] = root
        return root

    def potential(self, node: int) -> T:
        self.find_root(node)
        return self.__group.invert(self.__delta[node])

    def unite(self, node_u: int, node_v: int, delta: T) -> None:
        delta = self.__group.operation(self.potential(node_u), delta)
        delta = self.__group.operation(
            delta,
            self.__group.invert(self.potential(node_v)),
        )
        node_u, node_v = self.find_root(node_u), self.find_root(node_v)
        if node_u == node_v:
            return
        delta = self.__group.invert(delta)
        if self.__data[node_u] > self.__data[node_v]:
            node_u, node_v = node_v, node_u
            delta = self.__group.invert(delta)
        self.__data[node_u] += self.__data[node_v]
        self.__data[node_v] = node_u
        self.__delta[node_v] = delta

    def size(self, node: int) -> int:
        assert 0 <= node < len(self)
        return -self.__data[self.find_root(node)]

    def delta(self, node_u: int, node_v: int) -> T | None:
        if self.find_root(node_u) != self.find_root(node_v):
            return None
        return self.__group.operation(
            self.__group.invert(self.potential(node_u)),
            self.potential(node_v),
        )


def main() -> None:
    n, m = map(int, input().split())
    lrd = [tuple(map(int, input().split())) for _ in range(m)]
    group = Group[int](
        identity=lambda: 0,
        operation=lambda x, y: x + y,
        invert=lambda x: -x,
    )
    uf = PotentialUnionFind(group, n)
    for l, r, d in lrd:
        l -= 1
        r -= 1
        if uf.find_root(l) == uf.find_root(r) and uf.delta(l, r) != d:
            print("No")
            return
        uf.unite(l, r, d)
    print("Yes")


if __name__ == "__main__":
    main()
