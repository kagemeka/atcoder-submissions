#include <iostream>
#include <vector>


template <typename T>
class ChoosePascal {
  std::vector<std::vector<T>> c;

public:
  ChoosePascal(const int &n) : c(n, std::vector<T>(n)) {
    for (int i = 0; i < n; i++) c[i][0] = 1;
    for (int i = 1; i < n; i++) {
      for (int j = 1; j < i + 1; j++) {
        c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
      }
    }
  };

  const T operator() (const int &n, const int &k) {return k < 0 or n < k ? 0 : c[n][k];}
};


template <typename T, typename U>
T pow(T x, U n) {
  T y = 1;
  while (n) {
    if (n & 1) y *= x;
    x *= x;
    n >>= 1;
  }
  return y;
}

template<typename T>
class Modular {
  using Type = typename decay<decltype(T::value)>::type;
  template<typename U> static Type normalize(const U& x) {Type v = static_cast<Type>(x); return v % mod() + mod() % mod();}
  Type value;

public:
  constexpr Modular() : value() {}
  template<typename U> Modular(const U& x) {value = normalize(x);}

  const Type& operator()() const {return value;}
  template<typename U> explicit operator U() const {return static_cast<U>(value);}
  constexpr static Type mod() {return T::value;}
  Modular& operator+=(const Modular& rhs) {if ((value += rhs.value) >= mod()) value -= mod(); return *this;}
  Modular operator+(const Modular& rhs) const {return Modular(*this) += rhs;}
  Modular& operator-=(const Modular& rhs) {if ((value -= rhs.value) < 0) value += mod(); return *this;}
  Modular operator-(const Modular& rhs) const {return Modular(*this) -= rhs;}
  template<typename U> Modular& operator+=(const U& other) {return *this += Modular(other);}
  template<typename U> Modular& operator-=(const U& other) {return *this -= Modular(other);}
  Modular& operator++() {return *this += 1;}
  Modular& operator--() {return *this -= 1;}
  Modular operator++(int) {Modular res(*this); *this += 1; return res;}
  Modular operator--(int) {Modular res(*this); *this -= 1; return res;}
  Modular operator-() const {return Modular(-value);}
  Modular& operator*=(const Modular& rhs) {value *= rhs.value; value %= mod(); return *this;}
  Modular operator*(const Modular& rhs) const {return Modular(*this) *= rhs;}
  Modular inverse() const {return pow(*this, mod() - 2);}
  Modular& operator/=(const Modular& rhs) {*this *= rhs.inverse(); return *this;}
  Modular operator/(const Modular& rhs) const {return Modular(*this) /= rhs;}
  template<typename U>
  friend istream& operator>>(istream& is, Modular<U>& number) {return is >> number.value;}
  friend ostream& operator<< (ostream& os, const Modular& number) {return os << number.value;}
};

constexpr long long MOD = (long long)1e9 + 7;
using Mint = Modular<std::integral_constant<std::decay<decltype(MOD)>::type, MOD>>;



int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);

  auto choose = ChoosePascal<Mint>(1 << 10);

  int h, w, y, x, d, l;
  std::cin >> h >> w >> y >> x >> d >> l;

  Mint ans = choose(y * x, d + l);
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
    ans -= choose((y - cnt[0]) * (x - cnt[1]), d + l) * sign;
  }
  ans *= (long long)(h - y + 1) * (w - x + 1);
  ans *= choose(d + l, d);
  std::cout << ans << '\n';
}
