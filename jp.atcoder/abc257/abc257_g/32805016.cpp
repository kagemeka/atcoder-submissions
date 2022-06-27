#include <bits/stdc++.h>
using namespace std;

namespace types {
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
  using isize = std::make_signed<usize>::type;
  using f32 = float;
  using f64 = double;
  using f128 = __float128;

  template <typename T>
  using vec = std::vector<T>;

  template <typename T>
  using fn = std::function<T>;

} // namespace types

namespace morris_pratt_table_0_indexed {
  using namespace types;
  template <typename A>
  auto morris_pratt_table(const A& a) -> vec<int> {
    int n = a.size();
    vec<int> lb(n, 0);
    for (int i = 1, d = 0; i < n; ++i) {
      while (d != 0 && a[d] != a[i]) d = lb[d - 1];
      if (a[d] == a[i]) ++d;
      lb[i] = d;
    }
    return lb;
  }
} // namespace morris_pratt_table_0_indexed

auto main() -> int {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  using namespace types;
  string s, t;
  cin >> s >> t;
  usize n = s.size(), m = t.size();

  using morris_pratt_table_0_indexed::morris_pratt_table;
  auto lb = morris_pratt_table(s + '$' + t);
  usize i = m, k = 0;
  while (i > 0) {
    usize d = lb[n + i];
    if (!d) {
      cout << -1 << '\n';
      return 0;
    }
    i -= d;
    ++k;
  }

  cout << k << '\n';
}
