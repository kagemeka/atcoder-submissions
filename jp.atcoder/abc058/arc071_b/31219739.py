import sys
import numpy as np


def main() -> None:
    # \sum_i=0^{n-2}\sum_j={i+1}^{n-1}\sum_k=0^{m-2}\sum_l={k+1}^{m-1}
    # (x_j - x_i)(y_k - y_l)
    # = \sum_i=0^{n-2}\sum_j={i+1}^{n-1}(x_j - x_i)
    # \times \sum_k=0^{m-2}\sum_l={k+1}^{m-1}(y_k - y_l)

    # \sum_i=0^{n-2}\sum_j={i+1}^{n-1}(x_j - x_i)
    # = -\sum_i=0^{n-2}x_i(n-i-1) + \sum_i=0^{n-2}\sum_j={i+1}^{n-1}x_j

    n, m, *latter = map(int, sys.stdin.read().split())
    x, y = np.array(latter[:n]), np.array(latter[n:])

    MOD = 10**9 + 7

    def compute(x: np.ndarray) -> int:
        s = x.cumsum() % MOD
        n = x.size
        return (
            np.sum(
                s[-1] - s[:-1] - x[:-1] * (n - np.arange(n - 1) - 1) % MOD,
            )
            % MOD
        )

    print(compute(x) * compute(y) % MOD)


if __name__ == "__main__":
    main()
