def main() -> None:
    n = int(input())
    strings = [input() for _ in range(n)]

    _to_id = dict()

    def to_id(s: str) -> int:
        nonlocal _to_id
        _to_id[s] = _to_id.get(s, len(_to_id))
        return _to_id[s]

    edges = [(to_id(s[:3]), to_id(s[-3:])) for s in strings]
    # reverse graph
    # bfs
    m = len(_to_id)  # O(N)
    g = [[] for _ in range(m)]
    deg = [0] * m
    for i, j in edges:
        g[j].append(i)
        deg[i] += 1

    state = [-1] * m
    que = []
    for i in range(m):
        if deg[i] == 0:
            que.append(i)
            state[i] = 0  # lose node
    # win edge -> lose node
    # lose edge -> win node
    # draw edge -> draw node
    # win node -> at least one win edge
    # lose node -> no edge or all edges are lose.
    # draw node -> no win edge and at least one draw edge

    for i in que:
        for j in g[i]:
            if state[j] != -1:
                continue
            deg[j] -= 1
            if state[i] == 0:
                state[j] = 1
            elif state[i] == 1 and deg[j] == 0:
                state[j] = 0
            if state[j] != -1:
                que.append(j)

    for i in range(m):
        if state[i] == -1:
            state[i] = 2

    result_string = ("Aoki", "Takahashi", "Draw")
    for i, j in edges:
        s = state[j]
        res = result_string[s ^ 1] if s <= 1 else result_string[s]
        print(res)


if __name__ == "__main__":
    main()
