import bisect
import itertools


def main() -> None:
    # consider trying all the permutations and each adjacent pairs.
    # O(N!N)
    # for the continuous three camels,
    # if the first one and the second can be merged,
    # it's ok to merge them greedly.
    # note: if the two adjacent camels can be merged, their distance is 0.

    # sort lv pairs with l, and for each l, precompute min(v),
    # which is the minimum capacity of bridges
    # that have length more than or equal to v.
    # so that we can judge whether the two camels should be merged or not quickly.
    # O(\log{M}) with binary search.

    # O(N!N^2\log{M})

    n, m = map(int, input().split())
    weight = list(map(int, input().split()))

    lv = [tuple(map(int, input().split())) for _ in range(m)]
    lv.sort(key=lambda x: x[1])

    length, capacity = map(list, zip(*lv))
    for i in range(m - 1):
        length[i + 1] = max(length[i], length[i + 1])

    if max(weight) > min(capacity):
        print(-1)
        return
    inf = 1 << 60
    mn = inf
    for perm in itertools.permutations(range(n)):
        total_weight_from = [0] * n
        total_distance_from = [0] * n
        total_weight_from[0] = weight[perm[0]]
        for i in range(1, n):
            p = perm[i]
            min_dist_from_prev = 0
            for j in range(i):
                current_weight = total_weight_from[j] + weight[p]
                k = bisect.bisect_left(capacity, current_weight)
                min_dist_from_prev = max(
                    min_dist_from_prev,
                    0 if k == 0 else length[k - 1] - total_distance_from[j],
                )
                total_weight_from[j] = current_weight
            for j in range(i):
                total_distance_from[j] += min_dist_from_prev
            total_weight_from[i] = weight[p]
        mn = min(mn, total_distance_from[0])

    print(mn)


if __name__ == "__main__":
    main()
