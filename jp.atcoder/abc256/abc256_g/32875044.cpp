#include <bits/stdc++.h>

template <typename T>
auto extended_euclidean_gcd_recurse(T a, T b) -> std::tuple<T, T, T> {
  if (b == 0) {
    return {a, 1, 0};
  }
  auto [g, x, y] = extended_euclidean_gcd_recurse(b, a % b);
  return {g, y, x - a / b * y};
}

template <typename T>
auto euclidean_modular_gcd_inv(T mod, T n) -> std::pair<T, T> {
  auto [g, x, _] = extended_euclidean_gcd_recurse(n, mod);
  auto u = mod / g;
  assert(0 <= (x += (x < 0) * u) && x <= u);
  return {g, x};
}

template <typename T>
auto modular_inverse_euclidean(T mod, T n) -> T {
  auto [g, inv] = euclidean_modular_gcd_inv(mod, n);
  assert(g == 1);
  return inv;
}

template <typename T, T v, std::enable_if_t<2 <= v>* = nullptr>
struct const_modulus {
  static constexpr auto get() -> T { return v; }
};

struct default_id;
template <typename T, typename I = default_id>
struct static_modulus {
  static constexpr auto get() -> T { return value; }
  static constexpr void set(T v) {
    assert(1 <= v);
    value = v;
  }

private:
  static T value;
};
template <typename T, typename I>
T static_modulus<T, I>::value;

template <typename M>
class default_modular_arithmetic {

public:
  constexpr auto static mod() -> int { return M::get(); }

  constexpr auto static norm(int x) -> int {
    if (x < -mod() || mod() <= x) {
      x %= mod();
    }
    return x += (x < 0) * mod();
  }

  constexpr auto static add(int a, int b) -> int { return norm(a + b); }

  constexpr auto static neg(int a) -> int {
    auto v = norm(a);
    return v == 0 ? 0 : mod() - v;
  }

  constexpr auto static mul(int a, int b) -> int {
    return norm((long)a * b % mod());
  }

  constexpr auto static inv(int a) -> int {
    return modular_inverse_euclidean(mod(), norm(a));
  }
};

template <typename A> // Arithmetic
class modular_int {
  using T = typename std::decay<decltype(A::mod())>::type;

  T value;
  using Self = modular_int;
  constexpr static auto mod() -> T { return A::mod(); }

  template <typename U>
  constexpr static auto norm(U x) -> T {
    return (x % mod() + mod()) % mod();
  }

public:
  constexpr modular_int() : value() {}

  template <typename U>
  modular_int(const U& x) {
    value = norm(x);
  }

  auto operator()() const -> const T& { return value; }
  template <typename T>
  explicit operator T() const {
    return static_cast<T>(value);
  }

  auto operator-() const -> Self { return Self(A::neg(value)); }
  auto operator+=(const Self& rhs) -> Self& {
    value = A::add(value, rhs.value);
    return *this;
  }
  auto operator-=(const Self& rhs) -> Self& { return *this += -rhs; }
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
  auto operator*=(const Self& rhs) -> Self& {
    value = A::mul(value, rhs.value);
    return *this;
  }

  [[nodiscard]] auto inv() const -> Self { return Self(A::inv(value)); }

  auto operator/=(const Self& rhs) -> Self& { return *this *= rhs.inv(); }

  friend auto operator+(const Self& lhs, const Self& rhs) -> Self {
    return Self(lhs) += rhs;
  }
  friend auto operator-(const Self& lhs, const Self& rhs) -> Self {
    return Self(lhs) -= rhs;
  }
  friend auto operator*(const Self& lhs, const Self& rhs) -> Self {
    return Self(lhs) *= rhs;
  }
  friend auto operator/(const Self& lhs, const Self& rhs) -> Self {
    return Self(lhs) /= rhs;
  }
  friend auto operator==(const Self& lhs, const Self& rhs) -> bool {
    return lhs.value == rhs.value;
  }
  friend auto operator!=(const Self& lhs, const Self& rhs) -> bool {
    return lhs.value != rhs.value;
  }

  friend auto operator>>(std::istream& stream, Self& x) -> std::istream& {
    T v;
    stream >> v;
    x.value = norm(v);
    return stream;
  }
  friend auto operator<<(std::ostream& stream, const Self& x) -> std::ostream& {
    return stream << x.value;
  }
};

using mint1_000_000_007 =
    modular_int<default_modular_arithmetic<const_modulus<int, 1'000'000'007>>>;

using mint998_244_353 =
    modular_int<default_modular_arithmetic<const_modulus<int, 998'244'353>>>;

template <typename S>
auto factorial_table(int size) -> std::vector<S> {
  using namespace std;
  vector<S> a(size);
  iota(a.begin(), a.end(), 0);
  a[0] = 1;
  for (int i = 1; i < size - 1; ++i) a[i + 1] *= a[i];
  return a;
}

template <typename S>
auto inverse_factorial_table(int size) -> std::vector<S> {
  using namespace std;
  vector<S> a(size);
  iota(a.begin(), a.end(), 1);
  a[size - 1] = 1 / factorial_table<S>(size)[size - 1];
  for (int i = size - 1; i > 0; --i) a[i - 1] *= a[i];
  return a;
}

template <typename S>
class factorial_tables_frequent_ops {
  std::vector<S> fact, inv_fact;

public:
  factorial_tables_frequent_ops(int size) {
    fact = factorial_table<S>(size);
    inv_fact = inverse_factorial_table<S>(size);
  }

  auto p(int n, int k) -> S {
    if (k < 0 || n < k) return 0;
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

// T: semiring
template <typename T, typename M>
auto matrix_dot(const M& a, const M& b) -> M {
  assert(a[0].size() == b.size());
  int h = a.size(), w = b[0].size();
  M c(h, std::vector<T>(w));
  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      for (int k = 0; k < (int)a[0].size(); ++k) {
        c[i][j] += a[i][k] * b[k][j];
      }
    }
  }
  return c;
}

template <typename G, typename T, typename Z>
auto pow_semigroup(T x, Z n) -> T {
  assert(n >= 1);
  T y = x;
  --n;
  while (n) {
    if (n & 1) y = G::op(y, x);
    x = G::op(x, x);
    n >>= 1;
  }
  return y;
}

template <typename T>
using matrix = std::vector<std::vector<T>>;

using mint = mint998_244_353;

struct G {
  auto static op(const matrix<mint>& a, const matrix<mint>& b) -> matrix<mint> {
    return matrix_dot<mint>(a, b);
  }
};

auto main() -> int {
  using namespace std;

  long n;
  int d;
  cin >> n >> d;

  auto f = factorial_tables_frequent_ops<mint>(1 << 14);

  mint cnt = 0;
  for (int k = 0; k <= d + 1; k++) {
    matrix<mint> dp(2, vector<mint>(2, 0));
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 2; j++) {
        dp[i][j] = f.c(d - 1, k - i - j);
      }
    }
    dp = pow_semigroup<G>(dp, n);
    cnt += dp[0][0] + dp[1][1];
  }
  cout << cnt << endl;
}
