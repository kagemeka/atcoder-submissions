#include <bits/stdc++.h>
using namespace std;

#include <cstdint>
#include <functional>

using u8 = uint8_t;
using u16 = uint16_t;
using u32 = uint32_t;
using u64 = uint64_t;
using u128 = __uint128_t;
using i8 = int8_t;
using i16 = int16_t;
using i32 = int32_t;
using i64 = int64_t;
using i128 = __int128_t;
using usize = std::size_t;
using isize = std::make_signed<std::size_t>::type;
using f32 = float;
using f64 = double;
using f128 = __float128;

template <typename T>
using vec = std::vector<T>;

template <typename T>
using fn = std::function<T>;

template <typename T>
using G = vec<vec<T>>;

template <typename T, typename F, typename Cb>
auto floyd_warshall(G<T> g, F& f, Cb& cb) -> G<T> {
  int n = g.size();
  for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        g[i][j] = f(g[i][j], g[i][k], g[k][j]);
      }
    }
    cb(g);
  }
  return g;
}

auto main() -> int {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  int n, m;
  cin >> n >> m;
  const u64 inf = (u64)1 << 60;
  G<u64> g(n, vec<u64>(n, inf));
  for (int i = 0; i < n; ++i) g[i][i] = 0;
  for (int i = 0; i < m; ++i) {
    int a, b;
    u64 c;
    cin >> a >> b >> c;
    --a;
    --b;
    g[a][b] = c;
  }

  auto f = [](u64 x, u64 y, u64 z) { return min(x, y + z); };

  u64 s = 0;
  auto cb = [&](const G<u64>& g) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (g[i][j] != inf) s += g[i][j];
      }
    }
  };
  floyd_warshall(g, f, cb);

  cout << s << '\n';
}
