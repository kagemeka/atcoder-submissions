import sys
import numpy as np


def rotate_right_90(matrix: np.ndarray) -> np.ndarray:
    return matrix.copy()[::-1].T


def main() -> None:

    h, w, n, m = map(int, input().split())
    I = np.array(sys.stdin.read().split(), dtype=np.int64) - 1
    a, b = I[: 2 * n].reshape(n, 2).T
    c, d = I[2 * n :].reshape(m, 2).T
    is_light = np.zeros((h, w), np.bool8)
    is_wall = np.zeros((h, w), np.bool8)
    is_light[a, b] = True
    is_wall[c, d] = True

    def light_up(is_light: np.ndarray, is_wall: np.ndarray) -> np.ndarray:
        h, w = is_light.shape
        light_up = np.zeros((h, w), np.bool8)
        light_up[0] = is_light[0].copy()
        for i in range(1, h):
            light_up[i] = light_up[i - 1] & ~is_wall[i] | is_light[i]
        return light_up

    result = np.zeros((h, w), np.bool8)
    for _ in range(4):
        result |= light_up(is_light, is_wall)
        is_wall = rotate_right_90(is_wall)
        is_light = rotate_right_90(is_light)
        result = rotate_right_90(result)
    print(result.sum())


if __name__ == "__main__":
    main()
