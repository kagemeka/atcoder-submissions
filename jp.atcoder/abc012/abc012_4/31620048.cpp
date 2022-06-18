#include <algorithm>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <numeric>
#include <optional>
#include <stdexcept>
#include <type_traits>
#include <vector>

// return pair(g: gcd(mod, n), x: inverse(n / g) \mod (mod / g))
std::pair<int64_t, std::optional<int64_t>> extgcd_modinv(int64_t mod, int64_t n) {
  assert(mod > 1 && 0 <= n && n < mod);
  if (n == 0) return {mod, std::nullopt};
  auto a = n, b = mod;
  int64_t x00 = 1, x01 = 0;
  while (b) {
    auto q = a / b, r = a % b;
    x00 -= q * x01;
    std::swap(x00, x01);
    a = b;
    b = r;
  }
  auto gcd = a;
  if (x00 < 0) x00 += mod / gcd;
  assert(0 <= x00 && x00 < mod / gcd);
  return {gcd, x00};
}

template <uint32_t v, std::enable_if_t<2 <= v>* = nullptr> struct static_mod {
  static constexpr uint32_t get() { return value; }

private:
  static constexpr uint32_t value = v;
};

template <typename I> struct dynamic_mod {
  static constexpr uint32_t get() { return value; }
  static constexpr void set(uint32_t v) {
    assert(2 <= v);
    value = v;
  }

private:
  static uint32_t value;
};
template <typename I> uint32_t dynamic_mod<I>::value;

template <typename M> class modular {
  uint32_t value;
  constexpr static uint32_t mod() { return M::get(); }
  static uint32_t normalize(const int64_t& x) { return (x % mod() + mod()) % mod(); }

public:
  constexpr modular() : value() {}
  modular(const uint64_t& x) { value = normalize(x); }
  const uint32_t& operator()() const { return value; }
  template <typename T> explicit operator T() const { return static_cast<T>(value); }

  modular operator-() const { return modular(mod() - value); }
  modular& operator+=(const modular& rhs) {
    uint64_t v = (uint64_t)value + rhs.value;
    if (v >= mod()) v -= mod();
    value = v;
    return *this;
  }
  modular& operator-=(const modular& rhs) {
    uint64_t v = value;
    if (v < rhs.value) v += mod();
    value = v - rhs.value;
    return *this;
  }
  modular& operator++() { return *this += 1; }
  modular& operator--() { return *this -= 1; }
  modular operator++(int) {
    modular res(*this);
    *this += 1;
    return res;
  }
  modular operator--(int) {
    modular res(*this);
    *this -= 1;
    return res;
  }
  modular& operator*=(const modular& rhs) {
    value = (uint64_t)value * rhs.value % mod();
    return *this;
  }

  std::optional<modular> mul_inv() const {
    auto [g, inv] = extgcd_modinv(mod(), value);
    if (g != 1) return std::nullopt;
    return inv;
  }

  modular& operator/=(const modular& rhs) {
    if (auto inv = rhs.mul_inv()) {
      return *this *= *inv;
    } else {
      throw;
    }
  }

  friend modular operator+(const modular& lhs, const modular& rhs) { return modular(lhs) += rhs; }
  friend modular operator-(const modular& lhs, const modular& rhs) { return modular(lhs) -= rhs; }
  friend modular operator*(const modular& lhs, const modular& rhs) { return modular(lhs) *= rhs; }
  friend modular operator/(const modular& lhs, const modular& rhs) { return modular(lhs) /= rhs; }
  friend bool operator==(const modular& lhs, const modular& rhs) { return lhs.value == rhs.value; }
  friend bool operator!=(const modular& lhs, const modular& rhs) { return lhs.value != rhs.value; }

  friend std::istream& operator>>(std::istream& is, modular& x) {
    int64_t v;
    is >> v;
    x.value = normalize(v);
    return is;
  }
  friend std::ostream& operator<<(std::ostream& os, const modular& x) { return os << x.value; }
};

using mint1000000007 = modular<static_mod<1000000007>>;
using mint998244353 = modular<static_mod<998244353>>;

template <typename S, typename G> S pow_semigroup_recurse(const S& s, uint64_t n) {
  assert(n > 0);
  if (n == 1) return s;
  S x = pow_semigroup_recurse<S, G>(s, n >> 1);
  x = G::operate(x, x);
  if (n & 1) x = G::operate(x, s);
  return x;
}

template <typename S, typename G> S pow_semigroup(S s, uint64_t n) {
  assert(n > 0);
  S x = s;
  --n;
  while (n > 0) {
    if (n & 1) x = G::operate(x, s);
    s = G::operate(s, s);
    n >>= 1;
  }
  return x;
}

template <typename S, typename M> S pow_monoid(const S& s, uint64_t n) {
  if (n == 0) return M::identity();
  return pow_semigroup<S, M>(s, n);
}

template <typename S, typename G> S pow_group(const S& s, int64_t n) {
  return n >= 0 ? pow_monoid<S, G>(s, n) : pow_monoid<S, G>(G::invert(s), -n);
}

template <typename S, S (*op)(S, S)> std::vector<S> accumulate(std::vector<S> v) {
  for (int i = 0; i < (int)v.size(); ++i) {
    v[i + 1] = op(v[i], v[i + 1]);
  }
  return v;
}

template <typename T> T mul(T a, T b) { return a * b; }

template <typename S> std::vector<S> factorial_table(unsigned long int size) {
  assert(size > 0);
  std::vector<S> v(size);
  std::iota(v.begin(), v.end(), 0);
  v[0] = 1;
  return accumulate<S, mul<S>>(v);
}

template <typename S> std::vector<S> inverse_factorial_table(unsigned long int size) {
  std::vector<S> v(size);
  std::iota(v.begin(), v.end(), 1);
  v[size - 1] = 1 / factorial_table<S>(size)[size - 1];
  reverse(v.begin(), v.end());
  v = accumulate<S, mul<S>>(v);
  reverse(v.begin(), v.end());
  return v;
}

template <typename S> class combination {
  std::vector<S> fact, inv_fact;

public:
  combination(unsigned long int size) {
    fact = factorial_table<S>(size);
    inv_fact = inverse_factorial_table<S>(size);
  }
  S operator()(unsigned long int n, unsigned long int k) {
    if (n < k) return 0;
    return fact[n] * inv_fact[k] * inv_fact[n - k];
  }

  S inverse(unsigned long int n, unsigned long int k) {
    if (n < k) return 0;
    return inv_fact[n] * fact[k] * fact[n - k];
  }
};

template <typename S> class homogeneous_product {
  combination<S> choose;

public:
  homogeneous_product(unsigned long int size) : choose(size) {}
  S operator()(unsigned long int n, unsigned long int k) {
    return n == 0 ? 0 : choose(n + k - 1, k);
  }
};

template <typename mint> struct mod_mul {
  static mint operate(const mint& a, const mint& b) { return a * b; }
  static mint identity() { return 1; }
  static mint invert(const mint& a) { return 1 / a; }
};

template <typename T> std::vector<std::vector<T>> pascal_triangle(unsigned long int size) {
  std::vector<std::vector<T>> p(size, std::vector<T>(size, 0));
  for (unsigned long int i = 0; i < size; ++i) p[i][0] = 1;
  for (unsigned long int i = 1; i < size; ++i) {
    for (unsigned long int j = 1; j < size; ++j) {
      p[i][j] = p[i - 1][j - 1] + p[i - 1][j];
    }
  }
  return p;
}

template <typename T> class cached_pascal_triangle {
  std::unordered_map<unsigned long long int, T> cache;

public:
  cached_pascal_triangle() {}

  T operator()(unsigned long int n, unsigned long int k) {
    if (n < k) return 0;
    if (k == 0) return 1;
    unsigned long long int key = (unsigned long long int)n << 32 | k;
    if (cache.count(key) == 0) {
      cache[key] = (*this)(n - 1, k - 1) + (*this)(n - 1, k);
    }
    return cache[key];
  }
};

template <typename T>
std::vector<std::vector<T>> floyd_warshall(const std::vector<std::vector<T>>& min_edge_matrix) {
  auto dist = min_edge_matrix;
  unsigned long int n = dist.size();
  for (unsigned long int i = 0; i < n; ++i) assert(dist[i].size() == n);
  for (unsigned long int i = 0; i < n; ++i) {
    if (dist[i][i] < 0) {
      throw std::logic_error("negative cycle found.");
    }
    dist[i][i] = 0;
  }
  for (unsigned long int k = 0; k < n; ++k) {
    for (unsigned long int i = 0; i < n; ++i) {
      for (unsigned long int j = 0; j < n; ++j) {
        dist[i][j] = std::min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }
  for (unsigned long int i = 0; i < n; ++i) {
    if (dist[i][i] < 0) {
      throw std::logic_error("negative cycle found.");
    }
  }

  return dist;
}

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  using namespace std;

  int n, m;
  cin >> n >> m;

  constexpr int inf = 1 << 29;
  vector<vector<int>> dist(n, vector<int>(n, inf));
  for (int i = 0; i < m; ++i) {
    int a, b, t;
    cin >> a >> b >> t;
    --a;
    --b;
    dist[a][b] = t;
    dist[b][a] = t;
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      assert(dist[i][j] >= 0);
    }
  }

  dist = floyd_warshall(dist);

  int mn = inf;

  for (int i = 0; i < n; ++i) {
    mn = min(mn, *max_element(dist[i].begin(), dist[i].end()));
  }
  cout << mn << endl;
}
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
