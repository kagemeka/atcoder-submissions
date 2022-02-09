#include <bits/stdc++.h>
using namespace std;


template<typename T>
class Modular {

public:

using Type = typename decay<
  decltype(T::value)
>::type;

constexpr Modular() : value() {}

template<typename U>
Modular(const U& x) {
  value = normalize(x);
}

template<typename U>
static Type normalize(
  const U& x
) {
  Type v = static_cast<Type>(x);
  v = (v%mod() + mod()) % mod();
  return v;
}

const Type& operator() () const
{
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
  if (value < 0) {
    value += mod();
  }
  return *this;
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
  *this += Modular(other);
  return *this;
}

template<typename U>
Modular& operator-=(
  const U& other
) {
  *this -= Modular(other);
  return *this;
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
  value *= other.value;
  value %= mod();
  return *this;
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
  Modular a = pow(n>>1);
  a *= a;
  if (n&1) a *= *this;
  return a;
}

Modular inverse() const {
  return pow(mod() - 2);
}

Modular& operator/=(
  const Modular& other
) {
  *this *= other.inverse();
  return *this;
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


constexpr long long MOD
  = (long long)1e4 + 7;


using Mint = Modular<
  std::integral_constant<
    decay<decltype(MOD)>::type,
    MOD
  >
>;


template<typename T>
vector<vector<T>> identity(
  int n
) {
  vector<vector<T>> e(
    n,
    vector<T>(n)
  );
  for (int i = 0; i < n; i++) {
    e[i][i] = 1;
  }
  return e;
}


template<typename T>
vector<vector<T>> matrix_dot(
  const vector<vector<T>>& a,
  const vector<vector<T>>& b
) {
  int h0 = (int)a.size();
  int w0 = (int)a[0].size();
  int h1 = (int)b.size();
  int w1 = (int)b[0].size();
  assert(w0 == h1);
  vector<vector<T>> c(
    h0,
    vector<T>(w1)
  );
  for (int i = 0; i < h0; i++) {
    for (
      int j = 0; j < w1; j++
    ) {
      for (
        int k = 0; k < h1; k++
      ) {
        c[i][j] +=
          a[i][k] * b[k][j];
      }
    }
  }
  return c;
}


template<typename T>
vector<vector<T>> matrix_pow(
  const vector<vector<T>>& a,
  long long n
) {
  if (!n) {
    int m = (int)a.size();
    return identity<T>(m);
  }
  auto b = matrix_pow(a, n>>1);
  b = matrix_dot(b, b);
  if (n&1) b = matrix_dot(b, a);
  return b;
}


class Solver {

int n;
vector<vector<Mint>> c;
vector<vector<Mint>> a;

void prepare() {
  cin >> n;
  n--;
  c = {
    {1, 1, 1},
    {1, 0, 0},
    {0, 1, 0},
  };
  a = {
    {0},
    {0},
    {1},
  };
}


void solve() {
  if (n < 3) {
    cout << a[n][0] << '\n';
    return;
  }
  c = matrix_pow<Mint>(c, n-2);
  reverse(a.begin(), a.end());
  a = matrix_dot(c, a);
  cout << a[0][0] << '\n';
}


public:

void run() {
  prepare();
  solve();
}

};


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    Solver solver;
    solver.run();
  }

  return 0;
}
