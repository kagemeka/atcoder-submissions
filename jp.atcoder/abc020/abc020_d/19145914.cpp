#include <bits/stdc++.h>
using namespace std;

constexpr long long MOD = 1e9 + 7;

template<typename T>
class Modular {
public:

using Type = typename
  decay<decltype(T::value)>::type;

constexpr Modular() : value() {}

template<typename U>
Modular(const U& x) {
  value = normalize(x);
}

template<typename U>
static Type normalize(const U& x) {
  Type v = static_cast<Type>(x);
  return (v%mod() + mod()) % mod();
}

const Type& operator()() const {
  return value;
}

template<typename U>
explicit operator U() const {
  return static_cast<U>(value);
}

constexpr static Type mod() {
  return T::value;
}

Modular& operator+=(
  const Modular& other
) {
  value += other.value;
  if (value >= mod()) {
    value -= mod();
  }
  return *this;
}

Modular operator+(
  const Modular& other
) const {
  Modular res(*this);
  return res += other;
}

Modular& operator-=(
  const Modular& other
) {
  value -= other.value;
  if (value < 0) value += mod(); return *this;
}

Modular operator-(
  const Modular& other
) const {
  Modular res(*this);
  return res -= other;
}

template<typename U>
Modular& operator+=(
  const U& other
) {
  return *this += Modular(other);
}

template<typename U>
Modular& operator-=(
  const U& other
) {
  return *this -= Modular(other);
}

Modular& operator++() {
  return *this += 1;
}

Modular& operator--() {
  return *this -= 1;
}

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

Modular operator-() const {
  return Modular(-value);
}

Modular& operator*=(
  const Modular& other
) {
  (value *= other.value) %= mod(); return *this;
}

Modular operator*(
  const Modular& other
) const {
  Modular res(*this);
  return res *= other;
}

template<typename U>
Modular pow(const U& n) const {
  if (!n) return 1;
  Modular a = pow(n>>1); a *= a;
  if (n&1) a *= *this;
  return a;
}

Modular inverse() const {
  return pow(mod()-2);
}

Modular& operator/=(
  const Modular& other
) {
  return (*this) *= other.inverse();
}

Modular operator/(
  const Modular& other
) const {
  Modular res(*this);
  return res /= other;
}

template<typename U>
friend std::istream& operator>>(
  std::istream& is,
  Modular<U>& number
) {
  return is >> number.value;
}

friend std::ostream& operator<<(
  std::ostream& os,
  const Modular& number
) {
  return os << number.value;
}

private:
Type value;
};


using Mint = Modular<
  std::integral_constant<
    decay<decltype(MOD)>::type,
    MOD
  >
>;


template<typename T>
vector<T> find_divisors(T n) {
  vector<T> d(0);
  for (T i = 1; i*i <= n; i++) {
    if (n%i) {continue;}
    d.push_back(i);
    if (i*i != n) {
      d.push_back(n/i);
    }
  }
  sort(d.begin(), d.end());
  return d;
}


void solve(
  long long n,
  long long k
) {
  auto divs = find_divisors(k);
  reverse(divs.begin(), divs.end());
  int l = (int)divs.size();

  vector<Mint> s(l);
  for (int i = 0; i < l; i++) {
    long long d = divs[i];
    Mint q = n / divs[i];
    s[i] = (q + 1) * q * d / 2;
    for (int j = 0; j < i; j++) {
      if (divs[j]%d != 0) continue;
      s[i] -= s[j];
    }
  }
  Mint res = 0;
  for (int i = 0; i < l; i++) {
    res += s[i] / divs[i];
  }
  res *= k;
  cout << res << '\n';
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  long long n, k;
  cin >> n >> k;
  solve(n, k);

  return 0;
}
