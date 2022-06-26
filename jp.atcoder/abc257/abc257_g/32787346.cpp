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

namespace z_algorithm {
  using namespace types;

  template <typename A>
  auto z_algorithm(const A& a) -> vec<int> {
    int n = a.size();
    vec<int> lcp(n, 0);
    for (int i = 1, l = 0; i < n; ++i) {
      auto r = l + lcp[l];
      auto d = r <= i ? 0 : std::min(lcp[i - l], r - i);
      while (i + d < n && a[i + d] == a[d]) ++d;
      lcp[i] = d;
      if (r < i + d) l = i;
    }
    lcp[0] = n;
    return lcp;
  }
} // namespace z_algorithm

auto main() -> int {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);

  using namespace types;
  using z_algorithm::z_algorithm;

  string s, t;
  cin >> s >> t;
  usize n = s.size(), m = t.size();

  auto lcp = z_algorithm(s + '$' + t);
  usize r = 0, i = 0, k = 0;
  while (r < m) {
    auto nr = r;
    while (i <= r) {
      nr = max(nr, i + lcp[n + 1 + i]);
      ++i;
    }
    if (nr == r) {
      cout << -1 << '\n';
      return 0;
    }
    r = nr;
    ++k;
  }
  cout << k << '\n';
}
