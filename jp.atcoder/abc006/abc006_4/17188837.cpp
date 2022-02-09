#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>

using namespace std;


namespace GeometryTopology {
template<typename T>
double triangle_area(pair<T, T> p0, pair<T, T> p1, pair<T, T> p2, bool sign=true) {
  T x0 = p1.first - p0.first;
  T x1 = p2.first - p0.first;
  T y0 = p1.second - p0.second;
  T y1 = p2.second - p0.second;
  double s = (x0*y1 - x1*y0) / 2.0;
  if (sign) {return s;}
  return abs(s);
}
}
using namespace GeometryTopology;


// what field ?
template<typename T>
vector<T> LIS(vector<T> &a) {
  vector<T> b((int)a.size(), numeric_limits<T>::max());
  for (T &x : a) { b[lower_bound(b.begin(), b.end(), x) - b.begin()] = x;}
  return b;
}



namespace Algebra {
template<typename T>
vector<vector<T>> identity(int n) {
  vector<vector<T>> e(n, vector<T>(n));
  for (int i = 0; i < n; i++) e[i][i] = 1;
  return e;
}

template<typename T>
vector<vector<T>> dot(vector<vector<T>> &a, vector<vector<T>> &b) {
  int h = a.size(), w = b[0].size(), l = b.size();
  assert(a[0].size() == l);
  vector<vector<T>> c(h, vector<T>(w));
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      for (int k = 0; k < l; k++) {
        c[i][j] += a[i][k]*b[k][j];
      }
    }
  }
  return c;
}

template<typename T>
vector<vector<T>> matrix_pow(vector<vector<T>> a, T n, T mod=1e9+7) {
  int m = a.size();
  vector<vector<T>> b = identity<T>(m);
  while (n) {
    if (n&1) {b = dot(b, a);}
    n >>= 1;
    a = dot(a, a);
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < m; j++) {
        a[i][j] %= mod;
        b[i][j] %= mod;
      }
    }
  }
  return b;
}

template<typename T>
vector<vector<T>> bitwise_dot(vector<vector<T>> &a, vector<vector<T>> &b) {
  int h = a.size(), w = b[0].size(), l = b.size();
  assert((int)a[0].size() == l);
  vector<vector<T>> c(h, vector<T>(w));
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      for (int k = 0; k < l; k++) {
        c[i][j] ^= a[i][k]&b[k][j];
      }
    }
  }
  return c;
}

template<typename T>
vector<vector<T>> bitwise_mat_pow(vector<vector<T>> a, T n) {
  int m = a.size();
  vector<vector<T>> b = identity<T>(m);
  for (int i = 0; i < m; i++) b[i][i] = numeric_limits<T>::max();
  while (n) {
    if (n&1) b = bitwise_dot(b, a);
    n >>= 1; a = bitwise_dot(a, a);
  }
  return b;
}

template<typename T> T gcd(T a, T b) {return __gcd(a, b);}
template<typename T> T lcm(T a, T b) {return a/gcd(a, b)*b;}

}
using namespace Algebra;

namespace NumberTheory {

template<typename T>
struct PrimeNumber {
public:
const T N = 1e7;
bitset<(T)1e7> is_prime;
vector<T> prime_nums;
PrimeNumber(): prime_nums(0) {
  is_prime.set(); is_prime[0] = is_prime[1] = 0;
  for (T i = 2; i < N; i++) {
    if (!is_prime[i]) continue;
    for (T j = i*2; j < N; j += i) is_prime[j] = 0;
  }
  for (T i = 0; i < N; i++) {
    if (is_prime[i]) prime_nums.emplace_back(i);
  }
}
T& operator[](int i) {return prime_nums[i];}
bool operator()(T n) {return is_prime[n];}
map<T, int> factorize(T n) {
  map<T, int> cnt;
  if (n < 2) return cnt;
  for (T &p : prime_nums) {
    if (p*p > n) break;
    while (!(n%p)) {cnt[p]++; n /= p;}
    if (n==1) return cnt;
  }
  cnt[n] = 1; return cnt;
}

map<T, int> factorize_factorial(T n) {
  map<T, int> cnt;
  for (T i = 2; i < n+1; i++) {
    for (auto &x : factorize(i)) {cnt[x.first] += x.second;}
  }
  return cnt;
}
};

template<typename T>
vector<T> find_divisors(T n) {
  vector<T> d(0);
  for (int i = 1; i*i <= n; i++) {
    if (!(n%i)) {
      d.emplace_back(i);
      if (i*i != n) {d.emplace_back(n/i);}
    }
  }
  sort(d.begin(), d.end());
  return d;
}


}
using namespace NumberTheory;


namespace AtCoder {

namespace ABC001 {
void a() {int a, b; cin >> a >> b; cout << a-b << '\n';}
void b() {}
}

namespace ABC002 {
void a() {
  int x, y; cin >> x >> y;
  cout << max(x, y) << '\n';
}

void b() {
  set<char> vowels;
  for (auto &c : "aeiou") {vowels.insert(c);}
  string w;
  cin >> w;
  string s = "";
  for (char &c : w) {
    if (vowels.count(c)) {continue;}
    s += c;
  }
  cout << s << '\n';
}

void c() {
  int a, b, c, d, e, f;
  cin >> a >> b >> c >> d >> e >> f;
  pair<int, int> p0, p1, p2;
  p0 = make_pair(a, b);
  p1 = make_pair(c, d);
  p2 = make_pair(e, f);
  auto s = triangle_area(p0, p1, p2, false);
  cout << setprecision(16)  << s <<'\n';
}

void d() {
  int n, m; cin >> n >> m;
  vector<int> relations(n, 0);
  for (int i = 0; i < m; i++) {
    int x, y; cin >> x >> y; x--; y--;
    relations[x] |= 1<<y; relations[y] |= 1<<x;
  }
  int res = 0;
  for (int i = 0; i < 1<<n; i++) {
    int s = (1<<n) - 1, cnt = 0;
    for (int j = 0; j < n; j++) {
      if (i>>j&1) {s &= relations[j] | 1<<j; cnt++;}
    }
    if ((s&i)==i) {res = max(res, cnt);}
  }
  cout << res << '\n';
}
}

namespace ABC003 {
void a() {
  int n; cin >> n;
  cout << (n+1)*5000 << '\n';
}

void b() {
  set<char> atcoder;
  for (char &c : "atcoder"s) {atcoder.insert(c);}
  string s, t; cin >>s >> t;
  for (int i = 0; i < (int)s.size(); i++) {
    if (s[i] == t[i]) continue;
    if (s[i]=='@' && atcoder.count(t[i])) continue;
    if (atcoder.count(s[i]) && t[i]=='@') continue;
    cout << "You will lose" << '\n'; return;
  }
  cout << "You can win" << '\n';

}

void c() {
  int n, k; cin >> n >> k;
  vector<int> r(n);
  for (int i = 0; i < n; i++) cin >> r[i];
  sort(r.begin(), r.end(), greater<int>());
  double res = 0;
  for (int i = k-1; i > -1; i--) {res = (res + r[i])/2;}
  cout << setprecision(16) << res << '\n';
}

void d() {

}
}

namespace ABC004 {
void a() {
  int n; cin >> n; cout << n*2 << '\n';
}

void b() {
  int n = 4;
  vector<string> c(n);
  for (int i = 0; i < n; i++) getline(cin, c[i]);
  for (int i = n-1; i > -1; i--) {
    reverse(c[i].begin(), c[i].end());
    cout << c[i] << '\n';
  }
}

void c() {
  vector<int> a(6);
  for (int i = 0; i < 6; i++) a[i] = i+1;
  int n; cin >> n;
  n %= 30;
  for (int i = 0; i < n; i++) {
    swap(a[i%5], a[i%5+1]);
  }
  for (int &x : a) {cout << x;}
  cout << '\n';
}
}

namespace ABC005 {
void a() {
  int x, y; cin >> x >> y;
  cout << y/x << '\n';
}

void b() {
  int n; cin >> n;
  vector<int> t(n);
  for (int i = 0; i < n; i++) cin >> t[i];
  sort(t.begin(), t.end());
  cout << t[0] << '\n';
}

void c() {
  int t, n; cin >> t >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  int m; cin >> m;
  vector<int> b(m);
  for (int i = 0; i < m; i++) cin >> b[i];
  int i = 0;
  for (int &x : b) {
    while (i < n && x-a[i] > t) i++;
    if (i == n || a[i] > x) {cout << "no" << '\n'; return;}
    i++;
  }
  cout << "yes" << '\n';
}

void d() {
  int n; cin >> n;
  vector<vector<int>> d(n+1, vector<int>(n+1));
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
      cin >> d[i][j];
    }
  }
  int q; cin >> q;
  vector<int> p(q);
  for (int i = 0; i < q; i++) cin >> p[i];

  for (int i = 1; i <= n; i++) {
    for (int j = 1; j < n; j++) {
      d[i][j+1] += d[i][j];
    }
  }
  for (int j = 1; j <= n; j++) {
    for (int i = 1; i < n; i++) {
      d[i+1][j] += d[i][j];
    }
  }

  vector<int> res(n*n+1);
  for (int y = 1; y <= n; y++) {
    for (int x = 1; x <= n; x++) {
      for (int i = y; i <= n; i++) {
        for (int j = x; j <= n; j++) {
          int k = (i-y+1) * (j-x+1);
          res[k] = max(res[k], d[i][j]-d[i][x-1]-d[y-1][j]+d[y-1][x-1]);
        }
      }
    }
  }
  for (int i = 0; i < n*n; i++) {
    res[i+1] = max(res[i+1], res[i]);
  }
  for (int &x : p) {cout << res[x] << '\n';}
}
}

namespace ABC006 {
void a() {
  int n; cin >> n;
  if (n%3==0) {cout << "YES";} else {cout << "NO";}
  cout << '\n';
}

void b() {
  long long mod = 1e4 + 7;
  vector<vector<long long>> a = {
    {1, 1, 1},
    {1, 0, 0},
    {0, 1, 0},
  };
  long long n; cin >> n;
  a = matrix_pow(a, n-1, mod);
  cout << a[2][0] << '\n';
}

void c() {
  int n, m; cin >> n >> m;
  int a=0, b=0, c=0;
  if (m&1) {m -= 3; n -= 1; b = 1;}
  c = m/2 - n;
  a = n - c;
  if (a<0 || b<0 || c<0) {a = b = c = -1;}
  cout << a << ' ' << b << ' ' << c << '\n';

}

void d() {
  int n; cin >> n;
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> c[i];
  int inf = numeric_limits<int>::max();
  vector<int> a(n, inf);
  for (int &x : c) {
    *lower_bound(a.begin(), a.end(), x) = x;
  }
  int i = lower_bound(a.begin(), a.end(), inf) - a.begin();
  cout << n - i << '\n';
  // vector<int> lis = LIS(c);
  // cout << n - (lower_bound(lis.begin(), lis.end(), inf) - lis.begin()) << '\n';

}
}


namespace ABC009 {

void d() {
  uint k, m; cin >> k >> m;
  vector<vector<uint>> a(k, vector<uint>(1));
  vector<uint> c(k);

  for (uint i = 0; i < k; i++) cin >> a[i][0];
  for (uint i = 0; i < k; i++) cin >> c[i];
  vector<vector<uint>> d(k, vector<uint>(k)); d[0] = c;
  uint inf = numeric_limits<uint>::max();
  for (uint i = 1; i < k; i++) {d[i][i-1] = inf;}
  if (m <= k) {cout << a[m-1][0] << '\n'; return;}
  reverse(a.begin(), a.end());
  d = bitwise_mat_pow(d, m-k);
  cout << bitwise_dot(d, a)[0][0] << '\n';

}
}
}

namespace Codeforces {
}

int main() {
  ios::sync_with_stdio(false); cin.tie(0);

  AtCoder::ABC006::d();
  return 0;

}
