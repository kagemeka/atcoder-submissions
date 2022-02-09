#include <iostream>
#include <vector>


template <typename T>
class ModChoosePascal {
  std::vector<std::vector<T>> c;

public:
  ModChoosePascal(
    const int &n,
    const T &mod
  ) : c(n, std::vector<T>(n)) {
    for (int i = 0; i < n; i++) c[i][0] = 1;
    for (int i = 1; i < n; i++) {
      for (int j = 1; j < i + 1; j++) {
        c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod;
      }
    }
  };

  const T operator() (const int &n, const int &k) {
    if (k < 0 or n < k) return 0;
    return c[n][k];
  }
};



int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int mod = (int)1e9 + 7;
  auto choose = ModChoosePascal<long long>(1 << 10, mod);

  int h, w, y, x, d, l;
  std::cin >> h >> w >> y >> x >> d >> l;

  long long ans = choose(y * x, d + l);
  int n = 4;
  std::vector<int> cnt(2);
  for (int s = 1; s < 1 << n; s++) {
    cnt[0] = cnt[1] = 0;
    int sign = -1;
    for (int i = 0; i < n; i++) {
      if (~s >> i & 1) continue;
      cnt[i & 1] += 1;
      sign *= -1;
    }
    if (y - cnt[0] <= 0 or x - cnt[1] <= 0) continue;
    ans -= sign * choose((y - cnt[0]) * (x - cnt[1]), d + l);
    ans %= mod;
  }
  ans *= (long long)(h - y + 1) * (w - x + 1);
  ans %= mod;
  ans *= choose(d + l, d) % mod;
  std::cout << ans % mod << '\n';
}
