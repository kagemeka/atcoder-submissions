#include <bits/stdc++.h>
using namespace std;

template<typename T> auto extgcd(T a, T b) -> tuple<T, T, T> {
  if(b == 0) { return {a, 1, 0}; }
  auto [g, x, y] = extgcd(b, a % b);
  return {g, y, x - a / b * y};
}

template<typename T> auto mod_gcd_inv(T mod, T n) -> pair<T, T> {
  auto [g, x, _] = extgcd(n, mod);
  auto u = mod / g;
  assert(0 <= (x += (x < 0) * u) && x <= u);
  return {g, x};
}

template<typename T> auto modinv(T mod, T n) -> T {
  auto [g, inv] = mod_gcd_inv(mod, n);
  assert(g == 1);
  return inv;
}

template<typename T, T v, std::enable_if_t<(v > 0)>* = nullptr>
struct const_mod {
  static constexpr auto get() -> T { return v; }
};

template<typename M> struct modint {
  using T = typename std::decay<decltype(M::get())>::type;

  T value;

  using Self = modint;

  constexpr static auto m() -> T { return M::get(); }

  template<typename U> constexpr static auto norm(U x) -> T {
    T v = static_cast<T>(x);
    if(v < -m() || m() <= v) v %= m();
    return v + (v < 0) * m();
  }

  constexpr modint(): value() {}

  template<typename U> modint(U x): value(norm(x)) {}

  auto operator()() -> const T& { return value; }

  template<typename T> explicit operator T() const {
    return static_cast<T>(value);
  }

  auto operator+=(Self const& rhs) -> Self& {
    value += rhs.value;
    value -= (value >= m()) * m();
    return *this;
  }

  auto operator-() const -> Self {
    return Self(value == 0 ? value : m() - value);
  }

  auto operator*=(Self const& rhs) -> Self& {
    value *= rhs.value;
    if(value >= m()) value %= m();
    return *this;
  }

  [[nodiscard]] auto inv() const -> Self { return Self(modinv(m(), value)); }

  auto operator-=(Self const& rhs) -> Self& { return *this += -rhs; }

  auto operator/=(Self const& rhs) -> Self& { return *this *= rhs.inv(); }

  auto operator++() -> Self& { return *this += 1; }

  auto operator--() -> Self& { return *this -= 1; }

  auto operator++(int) -> Self {
    Self res(*this);
    *this += 1;
    return res;
  }

  auto operator--(int) -> Self {
    Self res(*this);
    *this -= 1;
    return res;
  }

  friend auto operator+(Self& lhs, Self& rhs) -> Self {
    return Self(lhs) += rhs;
  }

  friend auto operator-(Self& lhs, Self& rhs) -> Self {
    return Self(lhs) -= rhs;
  }

  friend auto operator*(Self& lhs, Self& rhs) -> Self {
    return Self(lhs) *= rhs;
  }

  friend auto operator/(Self& lhs, Self& rhs) -> Self {
    return Self(lhs) /= rhs;
  }

  friend auto operator==(Self const& lhs, Self const& rhs) -> bool {
    return lhs.value == rhs.value;
  }

  friend auto operator!=(Self const& lhs, Self const& rhs) -> bool {
    return lhs.value != rhs.value;
  }

  friend auto operator>>(std::istream& stream, Self& x) -> std::istream& {
    T v;
    stream >> v;
    x.value = norm(v);
    return stream;
  }

  friend auto operator<<(std::ostream& stream, Self const& x) -> std::ostream& {
    return stream << x.value;
  }
};

template<typename T, typename A> auto count_common_subsequences(A& a, A& b)
  -> T {
  int n = a.size(), m = b.size();
  vector<T> dp(m + 1, 1);
  for(int i = 0; i < n; i++) {
    for(int j = m - 1; j >= 0; j--)
      if(a[i] != b[j]) dp[j + 1] -= dp[j];
    for(int j = 0; j < m; j++) dp[j + 1] += dp[j];
  }
  return dp[m];
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;
  using mint = modint<const_mod<int, 1000000007>>;

  vector<mint> a(n), b(m);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < m; i++) cin >> b[i];

  auto res = count_common_subsequences<mint>(a, b);

  cout << res << endl;
}
