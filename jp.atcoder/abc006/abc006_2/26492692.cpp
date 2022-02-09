#include <iostream>
#include <vector>
#include <cassert>
using namespace std;


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
  using Type = typename std::decay<decltype(T::value)>::type;
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
  template<typename U> friend std::istream& operator>>(std::istream& is, Modular<U>& number) {return is >> number.value;}
  friend std::ostream& operator<< (std::ostream& os, const Modular& number) {return os << number.value;}
};

constexpr long long MOD = (long long)1e4 + 7;
using Mint = Modular<std::integral_constant<std::decay<decltype(MOD)>::type, MOD>>;



template <typename T>
std::vector<T> tribonacci_sequence(int n) {
  assert(n >= 3);
  std::vector<T> t(n);
  t[2] = 1;
  for (int i = 3; i < n; i++) t[i] = t[i - 1] + t[i - 2] + t[i - 3];
  return t;
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  auto t = tribonacci_sequence<Mint>(1 << 20);
  int n; cin >> n;
  cout << t[n - 1] << '\n';
}
