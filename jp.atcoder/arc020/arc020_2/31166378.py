def main() -> None:
    n, cost = map(int, input().split())
    colors = [int(input()) for _ in range(n)]
    K = 11
    count_odd = [0] * K
    count_even = [0] * K
    for i in range(n):
        if i & 1:
            count_odd[colors[i]] += 1
        else:
            count_even[colors[i]] += 1

    odd_stack = sorted(range(K), key=lambda x: count_odd[x])
    even_stack = sorted(range(K), key=lambda x: count_even[x])

    max_count = 0
    if odd_stack[-1] != even_stack[-1]:
        max_count = count_odd[odd_stack[-1]] + count_even[even_stack[-1]]
    max_count = max(max_count, count_odd[odd_stack[-2]] + count_even[even_stack[-1]])
    max_count = max(max_count, count_odd[odd_stack[-1]] + count_even[even_stack[-2]])
    print((n - max_count) * cost)


if __name__ == "__main__":
    main()
