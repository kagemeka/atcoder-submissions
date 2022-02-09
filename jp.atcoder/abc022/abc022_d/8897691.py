import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
a, b = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(2, n, 2)

def main():
    ga = np.mean(a, axis=0)
    gb = np.mean(b, axis=0)
    dist_ga_a = np.sqrt(np.sum(np.power(a - ga, 2), axis=1))
    dist_gb_b = np.sqrt(np.sum(np.power(b - gb, 2), axis=1))

    ans = np.sum(dist_gb_b) / np.sum(dist_ga_a)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
