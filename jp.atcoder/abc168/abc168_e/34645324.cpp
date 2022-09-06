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
template<typename M> struct modint {
  using T = typename std::decay<decltype(M::get())>::type;
  T value;
  using Self = modint;
  constexpr static auto m() -> T { return M::get(); }
  template<typename U> constexpr static auto norm(const U& x) -> T {
    T v = x;
    if(v < -m() || m() <= v) v %= m();
    return v + (v < 0) * m();
  }
  constexpr modint(): value() {}
  template<typename U> modint(const U& x): value(norm(x)) {}
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
  friend auto operator+(Self const& lhs, Self const& rhs) -> Self {
    return Self(lhs) += rhs;
  }
  friend auto operator-(Self const& lhs, Self const& rhs) -> Self {
    return Self(lhs) -= rhs;
  }
  friend auto operator*(Self const& lhs, Self const& rhs) -> Self {
    return Self(lhs) *= rhs;
  }
  friend auto operator/(Self const& lhs, Self const& rhs) -> Self {
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
template<typename T, T v, enable_if_t<(v > 0)>* = nullptr> struct const_mod {
  static constexpr auto get() -> T { return v; }
};
struct default_id;
template<typename T, typename I = default_id> struct static_mod {
  static constexpr auto get() -> T { return value; }
  static constexpr void set(T v) {
    assert(v > 0);
    value = v;
  }

private:
  static T value;
};
template<typename T, typename I> T static_mod<T, I>::value;
using mint1_000_000_007 = modint<const_mod<long, 1'000'000'007>>;
using mint998_244_353 = modint<const_mod<long, 998'244'353>>;
using default_static_mod = static_mod<long, default_id>;
using static_mint = modint<default_static_mod>;
template<typename S> auto factorial_table(int size) -> vector<S> {
  vector<S> a(size);
  iota(a.begin(), a.end(), 0);
  a[0] = 1;
  for(int i = 1; i < size - 1; ++i) a[i + 1] *= a[i];
  return a;
}
template<typename S> auto inverse_factorial_table(int size) -> vector<S> {
  vector<S> a(size);
  iota(a.begin(), a.end(), 1);
  a[size - 1] = 1 / factorial_table<S>(size)[size - 1];
  for(int i = size - 1; i > 0; --i) a[i - 1] *= a[i];
  return a;
}
template<typename S> class factorial_tables_frequent_ops {
public:
  vector<S> fact, inv_fact;
  factorial_tables_frequent_ops(int size) {
    fact = factorial_table<S>(size);
    inv_fact = inverse_factorial_table<S>(size);
  }
  auto p(int n, int k) -> S {
    if(k < 0 || n < k) return 0;
    return fact[n] * inv_fact[n - k];
  }
  auto c(int n, int k) -> S { return p(n, k) * inv_fact[k]; }
  auto h(int n, int k) -> S { return c(n - 1 + k, k); };
  auto inv(int n) -> S { return fact[n - 1] * inv_fact[n]; }
  auto inv_p(int n, int k) -> S {
    assert(0 <= k && k <= n);
    return inv_fact[n] * fact[n - k];
  }
  auto inv_c(int n, int k) -> S { return inv_p(n, k) * fact[k]; }
};
template<typename T, typename N> auto power(T x, N n) -> T {
  T y = 1;
  for(; n; x *= x, n >>= 1)
    if(n & 1) y *= x;
  return y;
}
auto main() -> int {
  int n;
  cin >> n;
  int zz = 0;
  using pi = pair<long, long>;
  map<pi, int> cnt;
  auto norm = [&](pi& x) {
    auto g = gcd(x.first, x.second);
    x.first /= g;
    x.second /= g;
    // if(x.first < 0) {
    //   x.second *= -1;
    //   x.first *= -1;
    // }
    pi y = {-1, 0};
    assert(x != y);
    if(x.second < 0) {
      x.second *= -1;
      x.first *= -1;
    }
  };
  auto inv = [&](pi x) -> pi {
    swap(x.first, x.second);
    x.first *= -1;
    norm(x);
    return x;
  };
  vector<pi> ab;
  for(int i = 0; i < n; i++) {
    long a, b;
    cin >> a >> b;
    if(a == 0 && b == 0) {
      zz++;
      continue;
    }
    pi x = {a, b};
    norm(x);
    cnt[x]++;
    ab.push_back(x);
  }
  if(n == 1) {
    cout << 1 << endl;
    return 0;
  }
  using mint = mint1_000_000_007;
  int const k = 1 << 18;
  vector<mint> pow2(k);
  pow2[0] = 1;
  for(int i = 0; i < k - 1; i++) pow2[i + 1] = pow2[i] * 2;
  mint p = 1;
  for(auto& x: ab) {
    auto y = inv(x);
    p *= pow2[cnt[x]] + pow2[cnt[y]] - 1;
    cnt[x] = cnt[y] = 0;
  }
  p -= 1;
  p += zz;
  cout << p << endl;
}
