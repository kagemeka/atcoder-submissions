#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

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

  const T operator() (const int &n, const int &k) {
    if (k < 0 or n < k) return 0;
    return c[n][k];
  }
};



template<typename T>
class Modular {
public:
  using Type = typename decay<decltype(T::value)>::type;
  constexpr Modular() : value() {}

  template<typename U>
  Modular(const U& x) {value = normalize(x);}

  template<typename U>
  static Type normalize(const U& x) {
    Type v = static_cast<Type>(x);
    return v % mod() + mod() % mod();
  }

  const Type& operator()() const {return value;}

  template<typename U>
  explicit operator U() const {return static_cast<U>(value);}

  constexpr static Type mod() {return T::value;}

  Modular& operator+=(const Modular& other) {
    value += other.value;
    if (value >= mod()) value -= mod();
    return *this;
  }

  Modular operator+ (const Modular& other) const {
    Modular res(*this);
    return res += other;
  }

  Modular& operator-=(const Modular& rhs) {
    value -= rhs.value;
    if (value < 0) value += mod();
    return *this;
  }

  Modular operator-(const Modular& rhs) const {
    Modular res(*this);
    return res -= rhs;
  }

  template<typename U>
  Modular& operator+=(const U& other) {
    *this += Modular(other);
    return *this;
  }

  template<typename U>
  Modular& operator-=(const U& other) {
    *this -= Modular(other);
    return *this;
  }

  Modular& operator++() {return *this += 1;}

  Modular& operator--() {return *this -= 1;}

  Modular operator++(int) {
    Modular res(*this);
    *this += 1;
    return res;
  }

  Modular operator--(int) {
    Modular res(*this);
    *this -= 1;
    return res;
  }

  Modular operator-() const {return Modular(-value);}

  Modular& operator*=(const Modular& other) {
    value *= other.value;
    value %= mod();
    return *this;
  }

  Modular operator*(const Modular& other) const {
    Modular res(*this);
    return res *= other;
  }


  template<typename U>
  Modular pow(const U& n) const {
    if (!n) return 1;
    Modular a = pow(n>>1);
    a *= a;
    if (n&1) a *= *this;
    return a;
  }

  Modular inverse() const {return pow(mod() - 2);}

  Modular& operator/=(const Modular& other) {
    *this *= other.invert();
    return *this;
  }

  Modular operator/(const Modular& other) const {
    Modular res(*this);
    return res /= other;
  }

  template<typename U>
  friend istream& operator>>(istream& is, Modular<U>& number) {
    return is >> number.value;
  }

  friend ostream& operator<< (
    ostream& os,
    const Modular& number
  ) {return os << number.value;}


private:
  Type value;

};


constexpr long long MOD = (long long)1e9 + 7;


using Mint = Modular<
  std::integral_constant<std::decay<decltype(MOD)>::type, MOD>
>;



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
