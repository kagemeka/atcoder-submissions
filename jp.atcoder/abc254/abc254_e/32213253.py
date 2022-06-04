def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")
        pprint.pprint(obj)


def main() -> None:

    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    added_to_que = [False] * n

    def compute(x: int, k: int) -> int:
        que = [x]
        added_to_que[x] = True
        history = [x]
        for _ in range(k):
            next_que = []
            for u in que:
                for v in g[u]:
                    if added_to_que[v]:
                        continue
                    next_que.append(v)
                    added_to_que[v] = True
            que = next_que
            history += que
        s = sum(history) + len(history)
        for x in history:
            added_to_que[x] = False
        return s

    q = int(input())
    res = []
    for _ in range(q):
        x, k = map(int, input().split())
        x -= 1
        s = compute(x, k)
        res.append(s)
    for s in res:
        print(s)


if __name__ == "__main__":
    main()
