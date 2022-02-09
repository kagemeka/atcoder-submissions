// #define _GLIBCXX_DEBUG
#include <bits/stdc++.h>

using namespace std;


/* Algebra */
namespace Algebra {

constexpr long long MOD = 1e9 + 7;
// constexpr long long MOD = 998244353;
const long double PI = acos(-1);
constexpr long double EPS = 1e-13;

template<typename T>
class Modular {

public:
using Type = typename decay<decltype(T::value)>::type;
constexpr Modular() : value() {}
template<typename U> Modular(const U& x) {value = normalize(x);}
template<typename U> static Type normalize(const U& x) {Type v = static_cast<Type>(x); return (v%mod()+mod())%mod();}

const  Type& operator()() const {return value;}
template<typename U> explicit operator U() const {return static_cast<U>(value);}
constexpr static Type mod() {return T::value;}

Modular& operator+=(const Modular& other) {if ((value += other.value) >= mod()) value -= mod(); return *this;}
Modular operator+(const Modular& other) const {Modular res(*this); return res += other;}
Modular& operator-=(const Modular& other) {if ((value -= other.value) < 0) value += mod(); return *this;}
Modular operator-(const Modular& other) const {Modular res(*this); return res -= other;}

template<typename U> Modular& operator+=(const U& other) {return *this += Modular(other);}
template<typename U> Modular& operator-=(const U& other) {return *this -= Modular(other);}
Modular& operator++() {return *this += 1;}
Modular& operator--() {return *this -= 1;}
Modular operator++(int) {Modular res(*this); *this += 1; return res;}
Modular operator--(int) {Modular res(*this); *this -= 1; return res;}
Modular operator-() const {return Modular(-value);}

Modular& operator*=(const Modular& other) {(value *= other.value) %= mod(); return *this;}
Modular operator*(const Modular& other) const {Modular res(*this); return res *= other;}

template<typename U>
Modular pow(const U& n) const {
  if (!n) return 1;
  Modular a = pow(n>>1); a *= a;
  if (n&1) a *= *this;
  return a;
}

Modular inverse() const {return pow(mod()-2);}
Modular& operator/=(const Modular& other) {return (*this) *= other.inverse();}
Modular operator/(const Modular& other) const {Modular res(*this); return res /= other;}

template<typename U>
friend std::istream& operator>>(std::istream& is, Modular<U>& number) {return is >> number.value;}
friend std::ostream& operator<<(std::ostream& os, const Modular& number) { return os << number.value;}

private:
Type value;
};


// using Mint2 = Modular<std::integral_constant<decay<decltype(MOD2)>::type, MOD2>>;
using Mint = Modular<std::integral_constant<decay<decltype(MOD)>::type, MOD>>;





template<typename T> int bit_length(T n);

vector<Mint> fact(1, 1), inv_fact(1, 1);

void make_fact(int n) {
  fact = vector<Mint>(n+1, 1);
  for (int i = 0; i < n; i++) {fact[i+1] = fact[i]*(i+1);}
  inv_fact = vector<Mint>(n+1, 1); inv_fact[n] = fact[n].inverse();
  for (int i = n; i > 0; i--) {inv_fact[i-1] = inv_fact[i]*i;}
}


template<typename T>
T pow(const T& a, const T& b) {
  T x = a, p = b, res = 1;
  while (p) {
    if (p&1) res *= x;
    x *= x; p >>= 1;
  }
  return res;
}



}
using namespace Algebra;







/* Combinatorics */
namespace Combinatorics {


template<typename T>
T next_combination(T s) {
  T x = s&-s, y = s+x;
  return ((s&~y)/x)>>1|y;
}


template<typename T>
vector<T> combinations(T a, int r) {
  int n = a.size();
  vector<T> res;
  if (r > n || r < 0) return res;
  vector<int> indices(r); for (int i = 0; i < r; i++) indices[i] = i;
  res.push_back(T(a.begin(), a.begin()+r));
  while (true) {
    bool flg = false;
    int i = r-1;
    for (; i > -1; i--) {if (indices[i] != i+n-r) {flg=true; break;}}
    if (!flg) {return res;}
    indices[i]++;
    for (int j = i+1; j < r; j++) {indices[j] = indices[j-1]+1;}
    T tmp(r); for (int j = 0; j < r; j++) tmp[j] = a[indices[j]];
    res.push_back(tmp);
  }
  return res;
}


Mint choose_mod(int n, int r) {
  if (r<0 || r>n) {return 0;}
  while ((int)fact.size() < n+1) {
    fact.push_back(fact.back() * (int)fact.size());
    inv_fact.push_back(fact.back().inverse());
  }
  return fact[n] * inv_fact[r] * inv_fact[n-r];
}


}
using namespace Combinatorics;



/* Geometry and Topology */
namespace GeometryTopology {

template<typename ...T>
struct Vector {
public:
Vector(T ... args){}
};


// to vector crossing algorithm later.
template<typename T>
double triangle_area(pair<T,T> p0, pair<T,T> p1, pair<T,T> p2, bool sign=true) {
  T x0 = p1.first - p0.first;
  T x1 = p2.first - p0.first;
  T y0 = p1.second - p0.second;
  T y1 = p2.second - p0.second;
  double s = (x0*y1 - x1*y0)/2.;
  return (sign ? s : abs(s));
}



/* Graph */
template<typename T>
struct Graph {
public:

Graph(int n=0): edges(n), nodes(n) {N = n;}
void add_edge(int u, int v, T weight=1, T cap=1) {
  edges[u].emplace(v, edge(weight, cap));
}

/* BFS */
vector<int> bfs(int src=0) {
  queue<int> q; q.push(src);
  lv = vector<int>(N, -1); lv[src] = 0;
  dist = vector<T>(N, INF); dist[src] = 0;
  parent = vector<int>(N, -1); parent[src] = src;
  while (!q.empty()) {
    int u = q.front(); q.pop();
    for (auto &p : edges[u]) {
      int v = p.first; edge e = p.second;
      if ((!e.capacity) || lv[v] != -1) continue;
      lv[v] = lv[u] + 1;
      dist[v] = dist[u] + e.weight;
      parent[v] = u;
      q.push(v);
    }
  }
  return depth = lv;
}

/* Dinic maximum flow algorithm. */
T dinic(int src, int sink) {
  function<T(int, T)> flow_to_sink;
  flow_to_sink = [&](int u, T flow_in) {
    if (u == sink) return flow_in;
    T flow = 0;
    for (auto &p : edges[u]) {
      int v = p.first; edge e = p.second;
      if ((!e.capacity) || lv[v] <= lv[u]) continue;
      T f = flow_to_sink(v, min(flow_in, e.capacity));
      if (!f) continue;
      edges[u].find(v)->second.capacity -= f;
      if (edges[v].count(u)) {
        edges[v].find(u)->second.capacity += f;
      } else {
        edges[v].emplace(u, edge(e.weight, f));
      }
      flow_in -= f; flow += f;
    }
    return flow;
  };

  T flow = 0;
  while (true) {
    bfs(src);
    if (lv[sink] == -1) return flow;
    flow += flow_to_sink(src, INF);
  }
}

/* Tree Doubling For Finding LCA */
void find_ancestors() {
  ancestors.push_back(parent);
  for (int i=0, l=bit_length(*max_element(depth.begin(), depth.end())); i < l; i++) {
    auto ancestor = *prev(ancestors.end());
    vector<int> nxt_ancestor(N);
    for (int u = 0; u < N; u++) {nxt_ancestor[u] = ancestor[ancestor[u]];}
    ancestors.push_back(nxt_ancestor);
  }
}

/* Find dist(u, v) on Tree.*/
T find_dist(int u, int v) {
  return dist[u]+dist[v] - 2*dist[find_lca(u,v)];
}

int find_lca(int u, int v) {
  int du = depth[u], dv = depth[v];
  if (du>dv) {swap(u,v); swap(du,dv);}
  int d = dv - du;
  for (int i=0, l=bit_length(d); i < l; i++) {
    if (d>>i&1) v = ancestors[i][v];
  }
  if (u==v) return u;
  for (int i=bit_length(du)-1; i > -1; i--) {
    int nu = ancestors[i][u],nv = ancestors[i][v];
    if (nu==nv) continue;
    u = nu, v = nv;
  }
  return parent[u];
}



/* Floyd Warshall shortest path algorithm.*/
vector<vector<T>> floyd_warshall() {
  vector<vector<T>> d(N, vector<T>(N, INF/10));
  for (int u = 0; u < N; u++) {
    d[u][u] = 0;
    for (auto &p : edges[u]) {
      int v = p.first; edge e = p.second;
      d[u][v] = e.weight;
    }
  }
  for (int w = 0; w < N; w++) {
    for (int u = 0; u < N; u++) {
      for (int v = 0; v < N; v++) {
        d[u][v] = min(d[u][v], d[u][w]+d[w][v]);
      }
    }
  }
  return d;
}

vector<T> dijkstra(int src) {
  using P = pair<T, int>;
  priority_queue<P, vector<P>, greater<P>> q; q.push(P(0, src));
  paths = vector<int>(N, 0); paths[src] = 1;
  vector<T> dist(N, INF/10); dist[src] = 0;
  vector<bool> visited(N, false);
  while (!q.empty()) {
    auto tmp = q.top(); q.pop();
    T d = tmp.first; int u = tmp.second;
    if (visited[u]) {continue;} visited[u] = true;
    for (auto &p : edges[u]) {
      int v = p.first; edge e = p.second;
      T dv = d + e.weight;
      if (dv>=dist[v]) {if (dv==dist[v]) {paths[v] = (paths[v]+paths[u])%MOD;} continue;}
      paths[v] = paths[u]; dist[v] = dv;
      q.push(P(dv, v));
    }
  }
  return dist;
}

vector<int> shortest_paths(int src) {
  dijkstra(src);
  return paths;
}

void change_cap(int u, int v, T c) {
  edges[u].find(v)->second.capacity = c;
}

// private:
struct edge {
  T weight, capacity;
  edge(T w=1, T c=1): weight(w), capacity(c) {}
};
struct node {};

vector<map<int, edge>> edges;
vector<node> nodes;

int N;

vector<int> lv;
vector<int> depth;
T INF = numeric_limits<T>::max();
vector<T> dist;
vector<int> parent;
vector<vector<int>> ancestors;

vector<int> paths;
};



struct UnionFind {
public:
UnionFind(int n=0): parent(n), rank(n), size(n, 1) {
  N = n;
  for (int i = 0; i < n; i++) parent[i] = i;
}

int find(int u) {
  if (parent[u]==u) return u;
  return parent[u] = find(parent[u]);
}

void unite(int u, int v) {
  u=find(u), v=find(v);
  if (u==v) return;
  if (rank[u]<rank[v]) swap(u,v);
  parent[v] = u;
  size[u] += size[v];
  rank[u] = max(rank[u], rank[v]+1);
}

bool same(int u, int v) {
  return find(u) == find(v);
}

vector<int> size;
vector<int> rank;
private:
int N;
vector<int> parent;
};

template<typename T>
struct Rectangle {
  T x1, y1, x2, y2;
  Rectangle(T _x1, T _y1, T _x2, T _y2): x1(_x1), y1(_y1), x2(_x2), y2(_y2) {}
  bool operator<(const Rectangle &r) const {
    if (this->x1 == r.x1) {
      if (this->y1 == r.y1) {
        if (this->x2 == r.x2) {
          return this->y2 < r.y2;
        }
        return this->x2 < r.x2;
      }
      return this->y1 < r.y1;
    }
    return this->x1 < r.x1;
  }
};

}
using namespace GeometryTopology;




template<typename T>
vector<T> LIS(vector<T> &a) {
  vector<T> b(a.size(), numeric_limits<T>::max());
  for (T &x : a) *lower_bound(b.begin(), b.end(), x) = x;
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
  assert((int)a[0].size() == l);
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

template<typename T> struct Kitamasa{};

template<typename T> int bit_length(T n) {int c = 0; while (n) {n >>= 1; c++;}; return c;}
template<typename T> int bit_count(T n) {int c = 0; while (n) {c += n&1; n >>= 1;}; return c;}

}






/* NumberTheory */
namespace NumberTheory {
template<typename T>
struct PrimeNumber {
public:
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

private:
const T N = 1e7;
bitset<(T)1e7> is_prime;
vector<T> prime_nums;

};

template<typename T>
vector<T> find_divisors(T n) {
  vector<T> d(0);
  for (T i = 1; i*i <= n; i++) {if (n%i) {continue;}; d.push_back(i); if (i*i != n) {d.push_back(n/i);}}
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
  vector<int> lis = LIS(c);
  int inf = numeric_limits<int>::max();
  cout << n - (lower_bound(lis.begin(), lis.end(), inf) - lis.begin()) << '\n';
}
}

namespace ABC007 {
void a() {
  int n; cin >> n; cout << n-1 << '\n';
}

void b() {
  string a; cin >> a;
  if (a=="a") {cout << -1 << '\n'; return;}
  cout << 'a' << '\n';

}

void c() {
  int r, c, sy, sx, gy, gx;
  cin >> r >> c >> sy >> sx >> gy >> gx;
  sy--; sx--; gy--; gx--;
  int src = sy*c + sx;
  int tgt = gy*c + gx;
  vector<string> maze(r);
  for (int i = 0; i < r; i++) cin >> maze[i];

  vector<pair<int, int>> dyx = {
    make_pair(-1, 0), make_pair(1, 0), make_pair(0, -1), make_pair(0, 1)
  };

  auto g = Graph<int>(r*c);

  for (int i = 1; i < r-1; i++) {
    for (int j = 1; j < c-1; j++) {
      if (maze[i][j] == '#') continue;
      int u = i*c + j;
      for (auto &d : dyx) {
        int y = i+d.first, x = j+d.second;
        if (maze[y][x] == '#') continue;
        int v = y*c + x;
        g.add_edge(u, v);
      }
    }
  }
  auto dist = g.bfs(src);
  cout << dist[tgt] << '\n';
}

void d() {
  auto cnt = [](int d) {
    return d <= 4 ? d : d-1;
  };

  auto f = [&](long long n) {
    auto x = to_string(n);
    int l = x.size();
    vector<vector<long long>> dp(l+1, vector<long long>(2, 0));
    dp[0][0] = 1;
    for (int i = 0; i < l; i++) {
      int d = x[i] - '0';
      dp[i+1][1] = dp[i][1]*8 + dp[i][0]*cnt(d);
      dp[i+1][0] = dp[i][0] * (d!=4 && d!=9);
    }
    return (n+1) - (dp[l][0]+dp[l][1]);
  };
  long long a, b; cin >> a >> b;
  cout << f(b) - f(a-1) << '\n';

}
}

namespace ABC008 {
void a() {
  int s, t; cin >> s >> t;
  cout << t-s+1 << '\n';
}

void b() {
  int n; cin >> n;
  map<string, int> votes;
  for (int i = 0; i < n; i++) {
    string s; cin >> s;
    votes[s]++;
  }
  auto res = vector<pair<string, int>>(votes.begin(), votes.end());
  sort(res.begin(), res.end(), [](pair<string, int> &a, pair<string, int> &b){
    return a.second > b.second;
  });
  cout << res[0].first << '\n';
}

void c() {
  int n; cin >> n;
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> c[i];
  double ex = .0;
  for (int i = 0; i < n; i++) {
    int div_cnt = 0;
    for (int j = 0; j < n; j++) {div_cnt += !(c[i]%c[j]);}
    ex += (div_cnt+1)/2/(double)div_cnt;
  }
  printf("%.16f\n", ex);
}

void d() {
  int h, w, n; cin >> h >> w >> n;
  vector<pair<int, int>> yx(n);
  for (int i = 0; i < n; i++) {
    int y, x; cin >> y >> x;
    yx[i] = make_pair(y,x);
  }

  map<Rectangle<int>, long long> cnt;

  function<long long(Rectangle<int>)> count;
  count = [&](Rectangle<int> r) {
    if (cnt.count(r)) return cnt[r];
    long long res = 0;
    int x1=r.x1, y1=r.y1, x2=r.x2, y2=r.y2;
    for (auto &p : yx) {
      int y=p.first, x=p.second;
      if (!(x1<=x && x<=x2 && y1<=y && y<=y2)) continue;
      long long tot = (x2-x1) + (y2-y1) + 1;
      tot += count(Rectangle<int>(x1,y1,x-1,y-1));
      tot += count(Rectangle<int>(x1,y+1,x-1,y2));
      tot += count(Rectangle<int>(x+1,y1,x2,y-1));
      tot += count(Rectangle<int>(x+1,y+1,x2,y2));
      res = max(res, tot);
    }
    return cnt[r] = res;
  };

  cout << count(Rectangle<int>(1,1,w,h)) << '\n';

}
}


namespace ABC009 {
void a() {
  int n; cin >> n;
  cout << (n+1)/2 << '\n';
}

void b() {
  int n; cin >> n;
  set<int> a;
  for (int i = 0; i < n; i++) {
    int x; cin >> x;
    a.insert(x);
  }
  auto it = a.end(); advance(it, -2);
  cout << *it << '\n';
}

void c() {
  int n, k; string s; cin >> n >> k >> s;
  using T = tuple<char, int, int>;
  vector<int> cost(n, 1);
  for (int i = 0; i < n; i++) {
    priority_queue<T, vector<T>, greater<T>> q;
    for (int j = i+1; j < n; j++) {
      if (s[j] < s[i]) q.push(make_tuple(s[j], cost[i]+cost[j], -j));
    }
    while (!q.empty()) {
      auto t = q.top(); q.pop();
      char ch; int c, j;
      tie(ch, c, j) = t;
      if (c > k) continue;
      j *= -1;
      swap(s[i], s[j]);
      cost[i] = cost[j] = 0;
      k -= c;
      break;
    }
  }
  cout << s << '\n';
}

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

namespace ABC010 {
void a() {
  string s; cin >> s;
  cout << s + "pp" << '\n';
}

void b() {
  int n; cin >> n;
  int tot = 0;
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    while (a%2 == 0 || a%3 == 2) {
      a--; tot++;
    }
  }
  cout << tot << '\n';
}

void c() {
  int sx, sy, gx, gy, t, v, n;
  cin >> sx >> sy >> gx >> gy >> t >> v >> n;
  vector<int> x(n), y(n);
  for (int i = 0; i < n; i++) {
    cin >> x[i] >> y[i];
  }
  for (int i = 0; i < n; i++) {
    int a = x[i], b = y[i];
    double dist = sqrt(pow(a-sx, 2)+pow(b-sy, 2)) + sqrt(pow(gx-a, 2)+pow(gy-b, 2));
    if (dist <= t*v) {cout << "YES" << '\n'; return;}
  }
  cout << "NO" << '\n';
}

void d() {
  int n, q, m; cin >> n >> q >> m;
  auto g = Graph<int>(n+1);
  for (int i = 0; i < q; i++) {
    int p; cin >> p;
    g.add_edge(p, n, 1, 1);
  }
  for (int i = 0; i < m; i++) {
    int a, b; cin >> a >> b;
    g.add_edge(a, b, 1, 1);
    g.add_edge(b, a, 1, 1);
  }
  cout << g.dinic(0, n) << '\n';

}
}

namespace ABC011 {
void a() {
  int n; cin >> n;
  cout << n%12 + 1 << '\n';
}
void b() {
  string s; cin >> s;
  for (int i = 1; i < (int)s.size(); i++) s[i] = tolower(s[i]);
  s[0] = toupper(s[0]);
  cout << s << '\n';
}
void c() {
  int n; cin >> n;
  set<int> ng;
  for (int i = 0; i < 3; i++) {
    int x; cin >> x;
    ng.insert(x);
  }
  if (ng.count(n)) {cout << "NO" << '\n'; return;}
  for (int i = 0; i < 100; i++) {
    bool flg = false;
    for (int d = -3; d <= -1; d++) {
      if (ng.count(n+d)) {continue;}
      n += d; flg = true; break;
    }
    if (!flg) {cout << "NO" << '\n'; return;}
    if (n <= 0) {cout << "YES" << '\n'; return;}
  }
  cout << "NO" << '\n';
}
void d() {
  int n, d, x, y; cin >> n >> d >> x >> y;
  x = abs(x); y = abs(y);
  if (x%d || y%d) {cout << 0 << '\n'; return;}
  x /= d; y /= d;
  vector<long double> fac(1001, .0); fac[0] = 1.;
  for (long long i = 0; i < 1000; i++) fac[i+1] = fac[i]*(i+1);
  long double res = .0;
  for (int i = 0; i <= n; i++) {
    for (int j = 0; i+j <= n; j++) {
      int k = i-y, l = j-x;
      if (k<0 || l<0 || i+j+k+l != n) continue;
      res += fac[n]/(fac[i]*fac[j]*fac[k]*fac[l]);
    }
  }
  for (int i = 0; i < n; i++) res /= 4.;
  cout << setprecision(16) << res << '\n';
  return ;

}
void d_2() {
  int n, d, x, y; cin >> n >> d >> x >> y;
  x = abs(x), y = abs(y);
  if (x%d || y%d) {cout << 0 << '\n'; return;}
  x /= d; y /= d;
  int r = n - (x+y);
  if (r<0 || r&1) {cout << 0 << '\n'; return;}

  using P = pair<int, int>;
  map<P, double> nCr;

  function<double(int, int)> c;
  c = [&](int n, int r) {
    if (r < 0 || r > n) return .0;
    if (r == 0) return 1.;
    P p = make_pair(n, r);
    if (nCr.count(p)) return nCr[p];
    return nCr[p] = c(n-1,r) + c(n-1, r-1)/4.;
  };
  double res = .0;
  for (int i = 0; i*2 <= r; i++) {
    int j = (r -i*2)/2;
    int south = i, north = y+i, east = j, west = x+j;
    res += c(n, south) * c(n-south, north) * c(n-south-north, east) * c(n-south-north-east, west);
  }
  cout << setprecision(16) << res << '\n';
}
}

namespace ABC012 {
void a() {
  int a, b; cin >> a >> b;
  cout << b << ' ' << a << '\n';
}
void b() {
  int n; cin >> n;
  int h, m, s;
  h = n/3600; n %= 3600;
  m = n/60; s = n%60;
  printf("%02d:%02d:%02d\n", h, m, s);

}
void c() {
  int n; cin >> n;
  n = 2025 - n;
  for (int i = 1; i < 10; i++) {
    if (n%i == 0) {
      int j = n/i;
      if (j > 9) continue;
      printf("%d x %d\n", i, j);
    }
  }
}

void d() {
  int n, m; cin >> n >> m;
  auto g = Graph<int>(n);
  for (int i = 0; i < m; i++) {
    int a, b, t; cin >> a >> b >> t;
    a--; b--;
    g.add_edge(a, b, t);
    g.add_edge(b, a, t);
  }
  int inf = numeric_limits<int>::max()/2;
  auto d = g.floyd_warshall();
  int res = inf;

  for (int i = 0; i < n; i++) {
    res = min(res, *max_element(d[i].begin(), d[i].end()));
  }
  cout << res << '\n';
}
}

namespace ABC013 {
void a() {
  char x; cin >> x;
  cout << x-'A'+1 << '\n';
}

void b() {
  int a, b; cin >> a >> b;
  int d = abs(b-a);
  cout << min(d, 10-d) << '\n';
}

void c() {
  long long n, h, a, b, c, d, e;
  cin >> n >> h >> a >> b >> c >> d >> e;

  auto f = [&](long long y) {
    long long x = (double)(n*e-h-(d+e)*y)/(b+e) + 1;
    x = min(max(x,0LL), n-y);
    return x;
  };

  long long res = numeric_limits<long long>::max();
  for (long long y = 0; y <= n; y++) {
    long long x = f(y);
    res = min(res, a*x + c*y);
  }
  cout << res << '\n';
}

void d() {
  int n, m, d; cin >> n >> m >> d;
  vector<int> a(m);
  for (int i = 0; i < m; i++) cin >> a[i];
  vector<int> res(n);
  for (int i = 0; i < n; i++) res[i] = i;
  for (int i = m-1; i > -1; i--) swap(res[a[i]-1], res[a[i]]);

  auto binary_method = [&](vector<int> a, int p) {
    vector<int> b(n);
    vector<int> nxt(n);
    for (int i = 0; i < n; i++) {b[i] = i;}
    while (p) {
      if (p&1) {
        for (int i = 0; i < n; i++) {b[i] = a[b[i]];}
      }
      p >>= 1;
      nxt = a;
      for (int i = 0; i < n; i++) {nxt[i] = a[nxt[i]];}
      a = nxt;
    }
    return b;
  };

  for (auto &x : binary_method(res, d)) {cout << x+1 << '\n';}
}
}

namespace ABC014 {
void a() {
  int a, b; cin >> a >> b;
  cout << (a+b-1)/b*b-a << '\n';
}
void b() {
  int n, x; cin >> n >> x;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  int tot = 0;
  for (int i = 0; i < n; i++) {
    if (x>>i&1) tot += a[i];
  }
  cout << tot << '\n';
}

void c() {
  int n; cin >> n;
  int m = 1001001;
  vector<int> res(m);
  for (int i = 0; i < n; i++) {
    int a, b; cin >> a >> b;
    res[a]++; res[b+1]--;
  }

  for (int i = 0; i < m; i++) res[i+1] += res[i];
  cout << *max_element(res.begin(), res.end()) << '\n';
}

void d() {
  int n; cin >> n;
  auto g = Graph<int>(n);
  for (int i = 0; i < n-1; i++) {
    int a, b; cin >> a >> b; a--; b--;
    g.add_edge(a, b);
    g.add_edge(b, a);
  }
  g.bfs(0);

  g.find_ancestors();
  int q; cin >> q;
  for (int i = 0; i < q; i++) {
    int a, b; cin >> a >> b; a--; b--;
    cout << g.find_dist(a, b)+1 << '\n';
  }
}
}

namespace ABC015 {
void a() {
  string a, b; cin >> a >> b;
  cout << (a.size()>b.size()?a:b) << '\n';
}
void b() {
  int n; cin >> n;
  int cnt = 0, tot = 0;
  for (int i = 0; i < n; i++) {
    int a; cin >> a;
    if (a) {tot += a; cnt++;}
  }
  cout << (tot+cnt-1)/cnt << '\n';
}

void c() {
  int n, k; cin >> n >> k;

  vector<vector<int>> t(n, vector<int>(n));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < k; j++) {
      cin >> t[i][j];
    }
  }


  bool res = false;
  function<void(int, int)> dfs;
  dfs = [&](int d, int s) {
    if (d==n) {res |= s==0; return;}
    for (int i = 0; i < k; i++) {dfs(d+1, s^t[d][i]);}
  };
  dfs(0,0);
  cout << (res ? "Found" : "Nothing") << '\n';
}

void d() {
  int w, n, m; cin >> w >> n >> m;
  vector<vector<int>> dp(m+1, vector<int>(w+1, 0));
  for (int i = 0; i < n; i++) {
    int a, b; cin >> a >> b;
    for (int j = m; j > 0; j--) {
      for (int k = a; k < w+1; k++) {
        dp[j][k] = max(dp[j][k], dp[j-1][k-a]+b);
      }
    }
  }
  cout << dp[m][w] << '\n';

}
}

namespace ABC016 {
void a() {
  int m, d; cin >> m >> d;
  cout << (m%d==0 ? "YES" : "NO") << '\n';
}

void b() {
  int a, b, c; cin >> a >> b >> c;
  bool f1 = a+b==c, f2 = a-b==c;
  cout << (f1&f2 ? "?" : f1 ? "+" : f2 ? "-" : "!") << '\n';
}

void c() {
  int n, m; cin >> n >> m;
  vector<int> f(n);
  for (int i = 0; i < m; i++) {
    int a, b; cin >> a >> b; a--; b--;
    f[a] |= 1<<b; f[b] |= 1<<a;
  }
  vector<int> res(n, 0);
  for (int i = 0; i < n; i++) {
    int tmp = 0; for (int j = 0; j < n; j++) tmp |= (f[i]>>j&1)*f[j];
    cout << bit_count(tmp & ~(f[i]|1<<i)) << '\n';
  }
}

void d() {
  // Vector<int> a(1);

}
}

namespace ABC017 {
void a() {
  int tot = 0;
  for (int i = 0; i < 3; i++) {
    int s, e; cin >> s >> e;
    tot += s*e/10;
  }
  cout << tot << '\n';
}

void b() {
  function<bool(string)> is_choku;

  set<string> cand;
  cand.insert("ch");
  cand.insert("o");
  cand.insert("k");
  cand.insert("u");

  is_choku = [&](string s) {
    if (s.empty()) {return true;}
    int l = s.size();
    if (cand.count(s.substr(l-1,1)) && is_choku(s.substr(0, l-1))) return true;
    if (l>=2 && s.substr(l-2,2)=="ch" && is_choku(s.substr(0,l-2))) return true;
    return false;
  };
  string x; cin >> x;
  cout << (is_choku(x) ? "YES" : "NO") << '\n';

}

void c() {
  int n, m; cin >> n >> m;
  int tot = 0;
  vector<int> a(m+1);
  for (int i = 0; i < n; i++) {
    int l, r, s; cin >> l >> r >> s; l--; r--;
    a[l] += s; a[r+1] -= s; tot += s;
  }
  for (int i = 0; i < m; i++) a[i+1] += a[i];
  cout << tot-*min_element(a.begin(), prev(a.end())) << '\n';

}

void d() {
  int n, m; cin >> n >> m;
  vector<int> prev(n+1);
  map<int, int> tmp;
  for (int i = 1; i < n+1; i++) {
    int f; cin >> f;
    prev[i] = tmp[f]; tmp[f] = i;
  }

  vector<int> dp(n+1); dp[0] = 1;
  int l=0, s=dp[0];
  for (int i = 1; i < n+1; i++) {
    while (l < prev[i]) {s = (s-dp[l])%MOD; s = (s+MOD)%MOD; l++;}
    dp[i] = s;
    s = (s+dp[i]) % MOD;
  }
  cout << dp[n] << '\n';
}
}

namespace ABC018 {
void a() {
  using P  = pair<int, int>;
  vector<P> a(3);
  for (int i = 0; i < 3; i++) {
    int j; cin >> j;
    a[i] = make_pair(i, j);
  }
  sort(a.begin(), a.end(), [](P &i, P &j){return i.second > j.second;});
  vector<int> res(3);
  for (int i = 0; i < 3; i++) res[a[i].first] = i+1;
  for (int &i : res) cout << i << '\n';
}

void b() {
  string s; int n; cin >> s >> n;
  while (n--) {
    int l, r; cin >> l >> r; l--; r--;
    reverse(s.begin()+l, s.begin()+r+1);
  }
  cout << s << '\n';
}

void c() {
  int r, c, k; cin >> r >> c >> k;
  int inf = numeric_limits<int>::max();
  vector<vector<int>> a(r+2, vector<int>(c+2));
  for (int i = 0; i < r; i++) {
    string s; cin >> s;
    for (int j = 0; j < c; j++) {
      a[i+1][j+1] = inf*(s[j]=='o');
    }
  }

  for (int i = 1; i < r+1; i++) {
    for (int j = 1; j < c+1; j++) {
      a[i][j] = min(a[i-1][j]+1, a[i][j]);
    }
  }
  for (int i = r; i > 0; i--) {
    for (int j = 1; j < c+1; j++) {
      a[i][j] = min(a[i+1][j]+1, a[i][j]);
    }
  }
  for (int j = 1; j < c+1; j++) {
    for (int i = 1; i < r+1; i++) {
      a[i][j] = min(a[i][j-1]+1, a[i][j]);
    }
  }
  for (int j = c; j > 0; j--) {
    for (int i = 1; i < r+1; i++) {
      a[i][j] = min(a[i][j+1]+1, a[i][j]);
    }
  }

  int tot = 0;
  for (int i = 1; i < r+1; i++) {
    for (int j = 1; j < c+1; j++) {
      tot += a[i][j]>=k;
    }
  }
  cout << tot << '\n';

}



void d() {
  int n, m, p, q, r; cin >> n >> m >> p >> q >> r;
  vector<vector<int>> g(n, vector<int>(m));
  while (r--) {
    int x, y, z; cin >> x >> y >> z; x--; y--;
    g[x][y] = z;
  }


  int res = 0;
  vector<int> S(n); for (int i = 0; i < n; i++) S[i]=i;
  for (auto &s : combinations(S, p)) {
    vector<int> tmp(m);
    for (int &i : s) {
      for (int j = 0; j < m; j++) tmp[j]+=g[i][j];
    }
    sort(tmp.begin(), tmp.end(), greater<int>());
    res = max(res, accumulate(tmp.begin(), tmp.begin()+q, 0));

  }
  cout << res << '\n';

}
}


namespace ABC019 {
void a() {
  vector<int> a(3); for (int i = 0; i < 3; i++) cin >> a[i];
  sort(a.begin(), a.end()); cout << a[1] << '\n';
}
void b() {
  string s; cin >> s;
  s += '$';
  string t = "";
  char prev = s[0]; int c = 1;
  for (int i=1, l=s.size(); i < l; i++) {
    if (s[i]==prev) {c++; continue;}
    t += prev+to_string(c); prev = s[i]; c = 1;
  }
  cout << t << '\n';
}

void c() {
  int n; cin >> n;
  set<int> s;
  while (n--) {
    int a; cin >> a;
    while ((a&1)^1) a >>= 1;
    s.insert(a);
  }
  cout << s.size() << '\n';
}

void d() {
  int n; cin >> n;
  int u = 1, dist = 0;
  auto inquire = [](int x, int y) {
    printf("? %d %d\n", x, y);
    int d; cin >> d; return d;
  };
  auto find = [&](int x) {
    int v;
    for (int i = 1; i <= n; i++) {
      if (i==x) continue;
      int d = inquire(u, i);
      if (d>dist) {dist=d, v=i;}
    }
    u = v;
  };
  find(u); find(u);
  printf("! %d\n", dist);

}
}

namespace ABC020 {
void a() {
  int q; cin >> q;
  cout << (q==1 ? "ABC" : "chokudai") << '\n';
}

void b() {
  string a, b; cin >> a >> b;
  cout << stoi(a+b)*2 << '\n';
}

void c() {
  int h, w, t; cin >> h >> w >> t;
  vector<vector<char>> s(h, vector<char>(w));
  int src=-1, tgt=-1;

  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cin >> s[i][j];
      if (s[i][j]=='S') {src = i*w+j; s[i][j] = '.';}
      if (s[i][j]=='G') {tgt = i*w+j; s[i][j] = '.';}
    }
  }

  auto dijkstra = [&](int x) {
    auto g = Graph<int>(h*w);
    for (int i = 0; i < h; i++) {
      for (int j = 0; j < w; j++) {
        int u = i*w+j;
        if (i>0) g.add_edge(u, (i-1)*w+j, s[i-1][j]=='#'?x:1);
        if (i<h-1) g.add_edge(u, (i+1)*w+j, s[i+1][j]=='#'?x:1);
        if (j>0) g.add_edge(u, i*w+j-1, s[i][j-1]=='#'?x:1);
        if (j<w-1) g.add_edge(u, i*w+j+1, s[i][j+1]=='#'?x:1);
      }
    }
    return g.dijkstra(src)[tgt] <= t;
  };

  auto binary_search = [&]() {
    int lo = 1, hi = t;
    while (lo+1 < hi) {
      int x = (lo+hi)/2;
      if (dijkstra(x)) {lo=x;} else {hi=x;}
    }
    return lo;
  };

  cout << binary_search() << '\n';


}

void d () {
  int n, k; cin >> n >> k;
  auto d = find_divisors<long long>(k);
  int l = d.size();
  vector<long long> s(l);
  for (int i = 0; i < l; i++) {s[i] = (1+n/d[i])*(n/d[i])/2 * d[i] % MOD;}
  for (int i = l-1; i > -1; i--) {
    for (int j = i+1; j < l; j++) {
      if (d[j]%d[i]==0) {s[i] = ((s[i]-s[j])%MOD+MOD)%MOD;}
    }
  }
  long long tot = 0;
  for (int i = 0; i < l; i++) {tot += s[i]*k/d[i]%MOD; tot %= MOD;}
  cout << tot << '\n';

}
}

namespace ABC021 {
void a() {
  int n; cin >> n;
  vector<int> s;
  for (int i = 0; i < 5; i++) {
    if (n>>i&1) {s.push_back(1<<i);}
  }
  cout << s.size() << '\n';
  for (auto &c : s) cout << c << '\n';
}

void b() {
  int n, a, b, k; cin >> n >> a >> b >> k;
  bitset<101> s; s.set(a); s.set(b);
  for (int i = 0; i < k; i++) {int p; cin >> p; s.set(p);}
  cout << ((int)s.count()==k+2 ? "YES": "NO") << '\n';
}

void c() {
  int n, a, b, m; cin >> n >> a >> b >> m; a--; b--;
  auto g = Graph<int>(n);
  while (m--) {
    int x, y; cin >> x >> y; x--; y--;
    g.add_edge(x,y);
    g.add_edge(y,x);
  }
  cout << g.shortest_paths(a)[b] << '\n';
}

void d() {
  int n, k; cin >> n >> k;
  make_fact(n+k);
  cout << choose_mod(n-1+k, k) << '\n';

}
}


namespace ABC022 {
void a() {
  int n, s, t; cin >> n >> s >> t;
  int w = 0;
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    int dw; cin >> dw;
    w += dw;
    cnt += (s <= w && w <= t);

  }
  cout << cnt << '\n';
}

void b() {
  int n; cin >> n;
  map<int, int> cnt;
  while (n--) {
    int a; cin >> a;
    cnt[a]++;
  }
  int tot = 0;
  for (auto& p : cnt) {
    tot += p.second-1;
  }
  cout << tot << '\n';
}

void c() {
  int n, m; cin >> n >> m;
  auto g = Graph<int>(n);

  int inf = numeric_limits<int>::max();
  vector<int> dist0(n, inf/10);

  while (m--) {
    int u, v, l; cin >> u >> v >> l; u--; v--;
    if (u==0) {dist0[v] = l; continue;}
    g.add_edge(u, v, l);
    g.add_edge(v, u, l);
  }
  auto dist = g.floyd_warshall();
  int res = inf/10;
  for (int i = 1; i < n-1; i++) {
    for (int j = i+1; j < n; j++) {
      res = min(res, dist0[i]+dist[i][j]+dist0[j]);
    }
  }
  cout << ((res == inf/10) ? -1 : res) << '\n';
}

void d() {

}
}


namespace ABC023 {
void a() {
  int x; cin >> x;
  cout << x/10 + x%10 << '\n';
}

void b() {
  int n; string s; cin >> n >> s;
  if ((n&1)^1) {cout << -1 << '\n'; return;}
  vector<char> a = {'a', 'b', 'c'};
  int i = ((1-n/2)%3+3)%3;
  for (auto& c : s) {
    if (c==a[i]) {i = (i+1)%3; continue;}
    cout << -1 << '\n'; return;
  }
  cout << n/2 << '\n';

}

void c() {
  int h, w, k, n; cin >> h >> w >> k >> n;
  vector<long long> r(n), c(n);
  for (int i = 0; i < n; i++) {cin >> r[i] >> c[i]; r[i]--; c[i]--;}
  vector<long long> rb(h), cb(w);
  for (int i = 0; i < n; i++) {rb[r[i]]++; cb[c[i]]++;}
  vector<long long> rbb(max(k+1, w+1)), cbb(max(k+1, h+1));
  for (int i = 0; i < h; i++) {rbb[rb[i]]++;}
  for (int i = 0; i < w; i++) {cbb[cb[i]]++;}

  long long tot = 0;
  for (int i = 0; i < k+1; i++) {tot += rbb[i]*cbb[k-i];}

  vector<long long> real(max(k+1, h+w));
  for (int i = 0; i < n; i++) {real[rb[r[i]]+cb[c[i]]-1]++;}
  tot += real[k]; tot -= real[k-1];
  cout << tot << '\n';


}

void d() {
  int n; cin >> n;
  vector<int> h(n), s(n);
  for (int i = 0; i < n; i++) {cin >> h[i] >> s[i];}

  auto is_ok = [&](long long x) {
    vector<long long> t_lim(n);
    for (int i = 0; i < n; i++) {
      long long d = x-h[i]; if (d<0) d -= (s[i]-1);
      t_lim[i] = d/s[i];
    }
    sort(t_lim.begin(), t_lim.end());
    for (int i = 0; i < n; i++) {
      if (t_lim[i] < i) return false;
    }
    return true;
  };

  auto binary_search = [&]() {
    long long lo = 0, hi = 1e14;
    while (lo+1 < hi) {
      long long x = (lo+hi)/2;
      if (is_ok(x)) {hi=x;} else {lo=x;}
    }
    return hi;
  };

  cout << binary_search() << '\n';

}
}


namespace ABC024 {
void a() {
  int a, b, c, k, s, t; cin >> a >> b >> c >> k >> s >> t;
  cout << s*a+t*b - (s+t>=k)*(s+t)*c << '\n';
}

void b() {
  int n, t; cin >> n >> t;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  int tot = t;
  for (int i = 0; i < n-1; i++) tot += min(t, a[i+1]-a[i]);
  cout << tot << '\n';
}

void c() {
  int n, d, k; cin >> n >> d >> k;
  vector<int> l(d), r(d);
  for (int i = 0; i < d; i++) cin >> l[i] >> r[i];
  vector<int> s(k), t(k);
  for (int i = 0; i < k; i++) cin >> s[i] >> t[i];

  vector<int> res(k, 0);
  for (int i = 0; i < d; i++) {
    for (int j = 0; j < k; j++) {
      if (s[j]==t[j] || s[j]<l[i] || s[j]>r[i]) continue;
      if (t[j]<l[i]) s[j] = l[i];
      else if (t[j]>r[i]) s[j] = r[i];
      else {s[j] = t[j]; res[j] = i+1;}
    }
  }
  for (auto& c : res) {cout << c << '\n';}
}

void d() {
  Mint a, b, c; cin >> a >> b >> c;
  Mint denom = a*b-b*c+c*a;
  cout << (b*c-a*c)/denom << ' ' << (b*c-a*b)/denom << '\n';
}
}

namespace ABC025 {
void a() {
  string s; int n; cin >> s >> n;
  n--;
  cout << ""s+s[n/5]+s[n%5] << '\n';
}

void b() {
  int n, a, b; cin >> n >> a >> b;
  unordered_map<string, int> c;
  while (n--) {
    string s; int d; cin >> s >> d;
    c[s] += min(max(d, a), b);
  }
  int res = c["East"] - c["West"];
  if (!res) {cout << 0 << '\n';}
  else if (res > 0) {printf("East %d\n", res);}
  else {printf("West %d\n", -res);}
}

void c() {
  vector<int> b(6), c(8);
  for (int i = 0; i < 6; i++) cin >> b[i];
  for (int i = 0; i < 8; i++) {if (!((i+1)%3)) {continue;} cin >> c[i];}

  int tot = accumulate(b.begin(), b.end(), 0) + accumulate(c.begin(), c.end(), 0);

  unordered_map<string, int> cache;
  function<int(string)> f;
  f = [&](string s) {
    if (cache.count(s)) return cache[s];
    int cand = 0, flg = 0;
    for (int i = 0; i < 9; i++) {if (s[i]=='0') {cand |= 1<<i; flg ^= 1;}}

    if (!cand) {
      int tot = 0;
      for (int i = 0; i < 6; i++) {tot += b[i]*(s[i]==s[i+3]);}
      for (int i = 0; i < 8; i++) {tot += c[i]*(s[i]==s[i+1]);}
      return cache[s] = tot;
    }
    vector<int> res;
    for (int i = 0; i < 9; i++) {
      if ((cand>>i&1)^1) continue;
      s[i] = '0'+(flg^1)+1; res.push_back(f(s)); s[i] = '0';
    }
    sort(res.begin(), res.end());
    return cache[s] = flg ? res.back() : res[0];
  };

  int a = f("000000000");
  cout << a << '\n' << tot-a << '\n';

}
}


namespace ABC026 {
void a() {
  int a; cin >> a;
  cout << (a/2)*((a+1)/2) << '\n';
}

void b() {
  int n; cin >> n;
  vector<int> r(n+1);
  for (int i = 1; i < n+1; i++) cin >> r[i];
  sort(r.begin(), r.end());
  vector<double> s(n+1);
  for (int i = 0; i < n+1; i++) s[i] = r[i]*r[i]*PI;
  double tot = .0;
  for (int i = n; i > 0; i-=2) {
    tot += s[i]-s[i-1];
  }
  cout << setprecision(16) << tot << '\n';

}

void c() {
  int n; cin >> n;
  vector<vector<int>> g(n);
  for (int i = 0; i < n-1; i++) {
    int b; cin >> b; b--;
    g[b].push_back(i+1);
  }
  function<int(int)> s;
  s = [&](int u) {
    if (g[u].empty()) return 1;
    vector<int> a;
    for (const auto& v : g[u]) {a.push_back(s(v));}
    sort(a.begin(), a.end());
    return a[0]+a.back()+1;
  };
  cout << s(0) << '\n';
}

void d() {
  int a, b, c; cin >> a >> b >> c;

  auto f = [&](double t) {
    return a*t+b*sin(c*t*PI)-100 > 0;
  };
  auto binary_search = [&]() {
    double lo=.0, hi=200.;
    while (hi-lo > EPS) {
      double t = (lo+hi)/2;
      if (f(t)) {hi=t;} else {lo=t;}
    }
    return hi;

  };
  cout << setprecision(16) << binary_search() << '\n';
}
}

namespace ABC027 {
void a() {
  vector<int> l(3);
  for (int i = 0; i < 3; i++) cin >> l[i];
  sort(l.begin(), l.end());
  cout << ((l[0]==l[1])? l[2] : l[0]) << '\n';
}

void b() {
  int n; cin >> n;
  vector<int> a(n);
  int tot = 0;
  for (int i = 0; i < n; i++) {cin >> a[i]; tot += a[i];}
  if (tot%n) {cout << -1 << '\n'; return;}
  int m = tot/n;
  int tmp = 0, c = 0, res = 0;
  for (int i = 0; i < n; i++) {
    c++; tmp += a[i];
    if (m*c != tmp) {res++; continue;}
    c = 0; tmp = 0;
  }
  cout << res << '\n';
}

void c() {
  long long n; cin >> n;
  int flg = (bit_length(n)-1)&1;
  long long x = 1; int t = 0;
  while (x <= n) {t++; x = (t&1)^flg ? 2*x+1 : 2*x;}
  cout << (t&1 ? "Aoki" : "Takahashi") << '\n';

}

void d() {
}
}

namespace ABC028 {
void a() {
  int n; cin >> n;
  cout << (n<60?"Bad":n<90?"Good":n<100?"Great":"Perfect") << '\n';
}

void b() {
  string s; cin >> s;
  unordered_map<char, int> cnt;
  for (const char& c : s) cnt[c]++;
  for (const char& c : "ABCDEF"s) cout << cnt[c] << (c=='F'? '\n': ' ');
}

void c() {
  int a, b, c, d, e; cin >> a >> b >> c >> d >> e;
  cout << max(a+d+e, b+c+e) << '\n';
}

void d() {
  long long n, k; cin >> n >> k;
  cout << setprecision(16) << (double)(3*2*(k-1)*(n-k) + 3*(n-1) + 1)/(n*n*n) << '\n';
}
}


namespace ABC029 {
void a() {
  string s; cin >> s;
  cout << s+"s" << '\n';
}

void b() {
  int n = 12;
  int tot = 0;
  while (n--) {
    string s; cin >> s;
    tot += (s.find('r') != string::npos);
  }
  cout << tot << '\n';
}

void c() {
  int n; cin >> n;
  queue<string> q;
  q.push("");
  while ((int)q.front().size() < n) {
    string s = q.front(); q.pop();
    for (const char& c : "abc"s) {q.push(s+c);}
  }
  while (!q.empty()) {cout << q.front() << '\n'; q.pop();}

}

void d() {
  int n; cin >> n;
  long long tot = 0;
  for (int i = 0; i < 9; i++) {
    tot += n/pow(10, i+1)*pow(10,i) + min(max(n%pow(10,i+1)-pow(10,i)+1, 0), pow(10,i));
  }
  cout << tot << '\n';
}
}

namespace ABC030 {
void a() {
  int a, b, c, d; cin >> a >> b >> c >> d;
  int l = b*c, r = d*a;
  cout << (l>r?"TAKAHASHI":l<r?"AOKI":"DRAW") << '\n';
}

void b() {
  int n; double m; cin >> n >> m;
  double d = abs((n%12+m/60)*30 - m*6);
  cout << min(d, 360-d) << '\n';
}

void c() {
  int n, m, x, y; cin >> n >> m >> x >> y;
  vector<int> a(n), b(m);
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < m; i++) cin >> b[i];
  int t = 0, flg=1, cnt=0;
  while (true) {
    if (flg) {
      int i = lower_bound(a.begin(), a.end(), t) - a.begin();
      if (i==n) break;
      t = a[i]+x;
    } else {
      int i = lower_bound(b.begin(), b.end(), t) - b.begin();
      if (i==m) break;
      t = b[i]+y;
      cnt++;
    }
    flg ^= 1;
  }
  cout << cnt << '\n';

}

void d() {
  int n, a; string k; cin >> n >> a >> k; a--;
  vector<int> b(n);
  for (int i = 0; i < n; i++) {cin >> b[i]; b[i]--;}
  vector<int> c(n, -1);


  for (int i = 0; i < n+1; i++) {
    if (to_string(i)==k) {cout << a+1 << '\n'; return;}
    if (c[a]==-1) {c[a] = i; a = b[a]; continue;}
    int l = i-c[a], d = c[a];
    reverse(k.begin(), k.end());
    int r = 1, m = k[0]-'0';
    for (int i = 1; i < (int)k.size(); i++) {r = r*10%l; m += r*(k[i]-'0')%l; m %= l;}
    m = ((m-d)%l+l)%l;
    while (m--) a = b[a];
    cout << a+1 << '\n'; return ;
  }
}
}

namespace ABC031 {
void a() {
  int a, d; cin >> a >> d;
  if (a > d) swap(a, d);
  cout << (a+1)*d << '\n';
}
void b() {
  int l, h, n; cin >> l >> h >> n;
  while (n--) {
    int a; cin >> a;
    cout << (a<l ? l-a : a<=h ? 0 : -1) << '\n';
  }
}
void c() {
  int n; cin >> n;
  vector<int> a(n+2);
  for (int i = 2; i < n+2; i++) cin >> a[i];
  for (int i = 2; i < n; i+=2) {a[i+2] += a[i];}
  for (int i = 3; i < n; i+=2) {a[i+2] += a[i];}

  auto score = [&](int i, int j, int &x, int &y) {
    i += 2; j += 2;
    if (i>j) swap(i,j);
    if ((j-i)&1) {x = a[j-1]-a[i-2], y = a[j]-a[i-1];}
    else {x = a[j]-a[i-2], y=a[j-1]-a[i-1];}
  };

  int inf = numeric_limits<int>::max();
  int res = -inf;
  for (int i = 0; i < n; i++) {
    int s = -inf, t = -inf;
    for (int j = 0; j < n; j++) {
      if (i==j) continue;
      int x, y; score(i, j, x, y);
      if (y>s) {s=y, t=x;}
    }
    res = max(res, t);
  }
  cout << res << '\n';
}

void d() {
  int k, n; cin >> k >> n;
  vector<string> v(n), w(n);
  for (int i = 0; i < n; i++) cin >> v[i] >> w[i];
  queue<string> q; q.push("");
  while ((int)q.front().size() < k) {
    string s = q.front(); q.pop();
    for (const char& c: "123"s) {q.push(s+c);}
  }

  while (!q.empty()) {
    string comb = q.front(); q.pop();
    unordered_map<int, string> s;
    for (int i = 0; i < n; i++) {
      int l = 0;
      for (const char& c : v[i]) {
        int d = c-'0'-1;
        int r = l+(comb[d]-'0');
        if (r > (int)w[i].size()) goto nxt;
        string t = w[i].substr(l, r-l);
        if (s.count(d) && s[d]!=t) goto nxt;
        s[d] = t;
        l = r;
      }
      if (l != (int)w[i].size()) goto nxt;
    }
    for (int i = 0; i < k; i++) {cout << s[i] << '\n';}; return;
    nxt: continue;
  }
}
}


namespace ABC032 {
void a() {
  int a, b, n; cin >> a >> b >> n;
  int l = lcm(a, b);
  cout << (n+l-1)/l*l << '\n';
}

void b() {
  string s; int k; cin >> s >> k;
  unordered_set<string> res;
  for (int i = 0; i < (int)s.size()-k+1; i++) {
    res.insert(s.substr(i, k));
  }
  cout << res.size() << '\n';
}

void c() {
  int n, k; cin >> n >> k;
  vector<int> s(n);
  for (int i = 0; i < n; i++) cin >> s[i];
  if (count(s.begin(), s.end(), 0)) {cout << n << '\n'; return;}
  if (k==0) {cout << 0 << '\n'; return;}

  long long res=0, tmp=1;
  for (long long l=0,r=0; r < n; r++) {
    tmp *= s[r];
    while (tmp > k) {tmp /= s[l]; l++;}
    res = max(res, r-l+1);
  }
  cout << res << '\n';
}

void d() {

}
}


namespace ABC033 {
void a() {
  string n; cin >> n;
  cout << (unordered_set<char>(n.begin(), n.end()).size()==1 ? "SAME" : "DIFFERENT") << '\n';
}

void b() {
  int n; cin >> n;
  using P = pair<string, int>;
  vector<P> a(n);
  int tot = 0;
  for (int i = 0; i < n; i++) {cin >> a[i].first >> a[i].second; tot += a[i].second;}
  sort(a.begin(), a.end(), [](P& a, P& b) {return a.second > b.second;});
  cout << (a[0].second <= tot/2 ? "atcoder" : a[0].first) << '\n';
}

void c() {
  string s; cin >> s;
  s += '+';
  int tot = 0;
  bool flg = false;
  for (int i = 0; i < (int)s.size(); i++) {
    if (s[i]=='+') {tot += !flg; flg = false;}
    flg |= (s[i]=='0');
  }
  cout << tot << '\n';
}

void d() {

}
}

namespace ABC034 {
void a () {
  int x, y; cin >> x >> y;
  cout << (y>x ? "Better" : "Worse") << '\n';
}

void b() {
  int n; cin >> n;
  cout << (n+1)-2*!(n&1) << '\n';
}

void c() {
  int w, h; cin >> w >> h;
  make_fact(w+h);
  cout << choose_mod(w+h-2, w-1) << '\n';
}

void d() {
  int n, k; cin >> n >> k;
  vector<double> w(n), p(n);
  for (int i = 0; i < n; i++) cin >> w[i] >> p[i];

  auto is_ok = [&](double x) {
    vector<double> a(n);
    for (int i = 0; i < n; i++) a[i] = w[i]*(p[i]-x);
    sort(a.begin(), a.end(), greater<double>());
    return accumulate(a.begin(), a.begin()+k, .0) >= 0;
  };

  auto binary_search = [&]() {
    double lo=.0, hi=100.1;
    while (hi-lo > EPS) {
      double x = (lo+hi)/2;
      if (is_ok(x)) {lo=x;} else {hi=x;}
    }
    return lo;
  };

  cout << setprecision(16) << binary_search() << '\n';
}
}

namespace ABC035 {

void a() {
  int w, h; cin >> w >> h;
  cout << (w*3==h*4 ? "4:3" : "16:9") << '\n';
}
void b() {
  string s; int t; cin >> s >> t;
  int x=0, y=0, z=0;
  for (const char& c : s) {
    switch (c) {
      case 'U': y++; break;
      case 'D': y--; break;
      case 'L': x--; break;
      case 'R': x++; break;
      default: z++;
    }
  }
  x = abs(x)+abs(y);
  cout << (t==1 ? x+z : max(x-z, (x-z)&1)) << '\n';
}

void c() {
  int n, q; cin >> n >> q;
  vector<int> a(n+1);
  while (q--) {
    int l, r; cin >> l >> r; l--; r--;
    a[l]++; a[r+1]--;
  }
  for (int i = 0; i < n; i++) {a[i+1] += a[i]; cout << (a[i]&1);}
  cout << '\n';
}

void d() {
  int n, m, t; cin >> n >> m >> t;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];

  auto g1 = Graph<long long>(n);
  auto g2 = Graph<long long>(n);
  while (m--) {
    int a, b, c; cin >> a >> b >> c; a--; b--;
    g1.add_edge(a, b, c);
    g2.add_edge(b, a, c);
  }
  auto d1 = g1.dijkstra(0);
  auto d2 = g2.dijkstra(0);
  long long res = 0;
  for (int i = 0; i < n; i++) {
    long long r = t-d1[i]-d2[i];
    if (r<0) continue;
    res = max(res, r*a[i]);
  }
  cout << res << '\n';

}
}

namespace ABC036 {
void a() {
  int a, b; cin >> a >> b;
  cout << (b+a-1)/a << '\n';
}

void b() {
  int n; cin >> n;
  vector<string> s(n);
  for (int i = 0; i < n; i++) cin >> s[i];
  for (int j = 0; j < n; j++) {
    for (int i = n-1; i > -1; i--) {
      cout << s[i][j];
    }
    cout << '\n';
  }
}
void c() {
  int n; cin >> n;
  using P = pair<int, int>;
  vector<P> a(n);
  for (int i = 0; i < n; i++) {cin >> a[i].first; a[i].second = i;}
  sort(a.begin(), a.end());

  vector<int> b(n);
  int prev = -1, i = -1;
  for (const P& p : a) {
    if (p.first != prev) i++;
    b[p.second] = i;
    prev = p.first;
  }
  for (int i = 0; i < n; i++) cout << b[i] << '\n';
}

void d() {
  int n; cin >> n;
  auto g = Graph<int>(n);
  for (int i = 0; i < n-1; i++) {
    int a, b; cin >> a >> b; a--; b--;
    g.add_edge(a, b); g.add_edge(b, a);
  }
  g.bfs(0);

  function<void(int, Mint&, Mint&)> count;
  count = [&](int u, Mint& white, Mint& black) {
    for (const auto& p : g.edges[u]) {
      int v = p.first;
      if (v==g.parent[u]) continue;
      Mint w=1, b=1; count(v, w, b);
      white *= (w+b); black *= w;
    }
  };

  Mint white=1, black=1; count(0, white, black);
  cout << white+black << '\n';
}
}


namespace ABC037 {
void a() {
  int a, b, c; cin >> a >> b >> c;
  cout << c/min(a,b) << '\n';
}

void b() {
  int n, q; cin >> n >> q;
  vector<int> a(n);
  while(q--) {
    int l, r, t; cin >> l >> r >> t; l--; r--;
    for (int i = l; i < r+1; i++) a[i] = t;
  }
  for (const int& x : a) cout << x << '\n';
}

void c() {
  int n, k; cin >> n >> k;
  vector<long long> a(n+1);
  for (int i = 1; i < n+1; i++) {cin >> a[i]; a[i] += a[i-1];}
  long long s = 0;
  for (int i = k; i < n+1; i++) s += a[i]-a[i-k];
  cout << s << '\n';
}

void d() {
  int h, w; cin >> h >> w;
  vector<int> a(h*w);
  for (int i = 0; i < h*w; i++) cin >> a[i];

  vector<Mint> c(h*w);
  function<Mint(int)> count;
  count = [&](int x) {
    if (c[x]) return c[x];
    c[x] = 1;
    int i = x/w, j = x%w;
    if (i>0 && a[x]>a[x-w]) c[x] += count(x-w);
    if (i<h-1 && a[x]>a[x+w]) c[x] += count(x+w);
    if (j>0 && a[x]>a[x-1]) c[x] += count(x-1);
    if (j<w-1 && a[x]>a[x+1]) c[x] += count(x+1);
    return c[x];
  };
  Mint s = 0;
  for (int i = 0; i < h*w; i++) s += count(i);
  cout << s << '\n';
}
}

namespace ABC038 {
void a() {
  string s; cin >> s;
  cout << (s.back()=='T' ? "YES" : "NO") << '\n';
}

void b() {
  int h1, w1, h2, w2; cin >> h1 >> w1 >> h2 >> w2;
  cout << ((h1==h2 || h1==w2 || w1==h2 || w1==w2) ? "YES" : "NO") << '\n';
}

void c() {
  int n; cin >> n;
  int inf = numeric_limits<int>::max();
  vector<int> a(n+1); a[n] = -1;
  for (int i = 0; i < n; i++) cin >> a[i];
  long long tot = n;
  int prev = inf;
  long long cnt = 0;
  for (const int& x : a) {
    if (x>prev) {cnt++;}
    else {tot += cnt*(cnt-1)/2; cnt = 1;}
    prev = x;
  }
  cout << tot << '\n';

}

void d() {
  int n; cin >> n;
  using P = pair<int, int>;
  vector<P> a(n);
  for (int i = 0; i < n; i++) cin >> a[i].first >> a[i].second;
  sort(a.begin(), a.end(), [](P& a, P& b){
    if (a.first == b.first) return a.second > b.second;
    return a.first < b.first;
  });
  vector<int> b(n);
  for (int i = 0; i < n; i++) b[i] = a[i].second;
  b = LIS(b);
  cout << lower_bound(b.begin(), b.end(), numeric_limits<int>::max()) - b.begin() << '\n';
}
}

namespace ABC039 {
void a() {
  int a, b, c; cin >> a >> b >> c;
  cout << 2*(a*b+b*c+c*a) << '\n';
}

void b() {
  int x; cin >> x;
  long long lo = 1, hi = 1e3;
  while (hi-lo > 1) {
    long long n = (lo+hi)/2;
    if (pow(n,4) <= x) {lo=n;} else {hi=n;}
  }
  cout << lo << '\n';
}
void c() {
  string board = "WBWBWWBWBWBW"; board = board+board+board;
  vector<string> cnv = {"Do", "", "Re", "", "Mi", "Fa", "", "So", "", "La", "", "Si"};
  string s; cin >> s;
  cout << cnv[board.find(s)] << '\n';
}
void d() {
  int h, w; cin >> h >> w;
  string s = "";
  for (int i = 0; i < h; i++) {string t; cin >> t; s+=t;}
  auto f = [&](int x, int& u, int& d, int& l, int& r) {
    int i = x/w, j = x%w;
    if (i>0) u = -w;
    if (i<h-1) d = w;
    if (j>0) l = -1;
    if (j<w-1) r = 1;
  };

  vector<bool> white(h*w);
  for (int i = 0; i < h*w; i++) {
    if (s[i]=='#') continue;
    int u=0, d=0, l=0, r=0; f(i, u, d, l, r);
    for (int dy = u; dy < d+1; dy+=w) {
      for (int dx = l; dx < r+1; dx++) {
        white[i+dy+dx] = true;
      }
    }
  }
  vector<bool> black(h*w);
  for (int i = 0; i < h*w; i++) {
    if (white[i]) continue;
    int u=0, d=0, l=0, r=0; f(i, u, d, l, r);
    for (int dy = u; dy < d+1; dy+=w) {
      for (int dx = l; dx < r+1; dx++) {
        black[i+dy+dx] = true;
      }
    }
  }

  for (int i = 0; i < h*w; i++) {
    if ((s[i]=='#') && (!black[i])) {cout << "impossible" << '\n'; return;}
  }
  cout << "possible" << '\n';
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      cout << (white[i*w+j] ? '.' : '#');
    }
    cout << '\n';
  }

}
}

namespace ABC040 {
void a() {
  int n, x; cin >> n >> x;
  cout << min(x-1, n-x) << '\n';
}
void b() {
  int n; cin >> n;
  int res = 1e9;
  for (int i = 1; i*i <= n; i++) {
    int j = n/i, r = n%i;
    res = min(res, j-i+r);
  }
  cout << res << '\n';
}
void c() {
  int n; cin >> n;
  vector<int> a(n+1), c(n+1);
  for (int i = 1; i < n+1; i++) {cin >> a[i];}; a[0] = a[1];
  for (int i = 2; i < n+1; i++) {
    c[i] = min(c[i-2]+abs(a[i]-a[i-2]), c[i-1]+abs(a[i]-a[i-1]));
  }
  cout << c[n] << '\n';
}

void d() {
  int n, m; cin >> n >> m;
  using T = tuple<int, int, int>;
  priority_queue<T> que;
  while (m--) {
    int a, b, y; cin >> a >> b >> y; a--; b--;
    que.push(T(2*y, a, b));
  }
  int q; cin >> q;
  for (int i = 0; i < q; i++) {
    int v, y; cin >> v >> y; v--;
    que.push(T(2*y+1, v, i));
  }
  auto uf = UnionFind(n);
  vector<int> res(q);
  while (!que.empty()) {
    T t = que.top(); que.pop();
    int y, i, j; tie(y, i, j) = t;
    if (y&1) {res[j] = uf.size[uf.find(i)];}
    else uf.unite(i, j);
  }
  for (const int& x : res) cout << x << '\n';
}
}

namespace ABC041 {
void a() {
  string s; int i; cin >> s >> i;
  cout << s[i-1] << '\n';
}
void b() {
  Mint a, b, c; cin >> a >> b >> c;
  cout << a*b*c << '\n';
}
void c() {
  int n; cin >> n;
  using P = pair<int, int>;
  vector<P> a(n);
  for (int i = 0; i < n; i++) {cin >> a[i].first; a[i].second = i+1;}
  sort(a.begin(), a.end(), greater<P>());
  for (int i = 0; i < n; i++) cout << a[i].second << '\n';
}
void d() {
  int n, m; cin >> n >> m;
  vector<int> g(n);
  while (m--) {
    int x, y; cin >> x >> y; x--; y--;
    g[x] |= 1<<y;
  }
  vector<long long> res(1<<n); res[0] = 1;
  for (int i = 0; i < 1<<n; i++) {
    for (int j = 0; j < n; j++) {
      if (!(i>>j&1) || g[j]&i) continue;
      res[i] += res[i&~(1<<j)];
    }
  }
  cout << res.back() << '\n';
}
}

namespace ABC042 {
void a() {
  int n = 3;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  cout << ((a[0]==5 && a[1]==5 && a[2]==7) ? "YES" : "NO") << '\n';
}
void b() {
  int n, l; cin >> n >> l;
  vector<string> s(n);
  for (int i = 0; i < n; i++) cin >> s[i];
  sort(s.begin(), s.end());
  for (const string& t : s) cout << t;
  cout << '\n';
}
void c() {
  int n, k; cin >> n >> k; n--;
  unordered_set<int> dis;
  for (int i = 0; i < k; i++) {int d; cin >> d; dis.insert(d);}
  while (++n) {
    int x = n;
    while (x) {
      if (dis.count(x%10)) {goto nxt;}
      x /= 10;
    }
    cout << n << '\n'; return;
    nxt: continue;
  }
}
void d() {
  int h, w, a, b; cin >> h >> w >> a >> b;
  make_fact(h+w);
  Mint ng = 0;
  for (int i = 0; i < a; i++) {ng += choose_mod(b-1+h-1-i, b-1) * choose_mod(i+w-1-b, i);}
  cout << choose_mod(h+w-2, h-1)-ng << '\n';
}
}

namespace ABC043 {
void a() {
  int n; cin >> n;
  cout << (1+n)*n/2 << '\n';
}
void b() {
  string s; cin >> s;
  string t = "";
  for (const char& c : s) {
    if (c!='B') {t += c; continue;}
    if (!t.empty()) t.pop_back();
  }
  cout << t << '\n';
}
void c() {
  int n; cin >> n;
  int s = 0;
  vector<int> a(n); for (int i = 0; i < n; i++) {cin >> a[i]; s += a[i];}
  int x = round((double)s/n);
  s = 0;
  for (const int& v : a) {s += pow(x-v, 2);}
  cout << s << '\n';
}
void d() {
  string s; cin >> s; int n = s.size();
  for (int i = 0; i < n-1; i++) {
    if (s[i]==s[i+1]) {printf("%d %d\n", i+1, i+2); return;}
  }
  for (int i = 1; i < n-1; i++) {
    if (s[i-1]==s[i+1]) {printf("%d %d\n", i, i+2); return;}
  }
  cout << -1 << ' ' << -1 << '\n';
}
}


namespace ABC044 {
void a() {
  int n, k, x, y; cin >> n >> k >> x >> y;
  cout << min(n,k)*x + max(0,n-k)*y << '\n';
}
void b() {
  string w; cin >> w;
  unordered_map<char, int> cnt;
  for (const char& c : w) {cnt[c] ^= 1;}
  for (const auto& p : cnt) {
    if (p.second) {cout << "No" << '\n'; return;}
  }
  cout << "Yes" << '\n';
}
void c() {
  int n, a; cin >> n >> a;
  vector<int> x(n);
  for (int i = 0; i < n; i++) {cin >> x[i]; x[i] -= a;}
  unordered_map<int, long long> dp; dp[0] = 1;
  for (int i = 0; i < n; i++) {
    auto ndp = dp;
    for (const auto& p : dp) ndp[p.first+x[i]] += p.second;
    dp = ndp;
  }
  cout << dp[0]-1 << '\n';
}
}

namespace ABC045 {
void a() {
  int a, b, h; cin >> a >> b >> h;
  cout << (a+b)*h/2 << '\n';
}
void b() {
  map<char, string> s;
  for (const char& c: "abc"s) {
    cin >> s[c];
    reverse(s[c].begin(), s[c].end());
  }
  char cur = 'a';
  while (1) {
    if (s[cur].empty()) {cout << string(1, toupper(cur)) << '\n'; return;}
    auto nx = s[cur].back(); s[cur].pop_back();
    cur = nx;
  }
}
void c() {
  string s; cin >> s;
  int n = (int)s.size();
  auto c = [](int l) {return 1<<max(0,l-1);};
  long long tot = 0;
  for (int i = 0; i < n; i++) {
    long long d = 0;
    for (int j = i; j < n; j++) {
      d = 10*d + (s[j]-'0');
      tot += d * c(i) * c(n-1-j);
    }
  }
  cout << tot << '\n';
}
void d() {
  long long h, w, n; cin >> h >> w >> n;
  unordered_map<long long, int> mp;
  while (n--) {
    int a, b; cin >> a >> b; a--; b--;
    for (int i = -1; i < 2; i++) {
      for (int j = -1; j < 2; j++) {
        long long y = a+i, x = b+j;
        if (y<=0 || y>=h-1 || x<=0 || x>=w-1) continue;
        mp[y*w+x]++;
      }
    }
  }
  vector<long long> cnt(10); cnt[0] = (h-2)*(w-2);
  for (const pair<long long, int>& p : mp) {cnt[p.second]++; cnt[0]--;}
  for (int i = 0; i < 10; i++) cout << cnt[i] << '\n';
}
}

namespace ABC046 {
void a() {
  int n = 3;
  set<int> s;
  while (n--) {
    int x; cin >> x;
    s.insert(x);
  }
  cout << s.size() << '\n';
}
void b() {
  int n, k; cin >> n >> k;
  cout << k*pow(k-1, n-1) << '\n';
}
void c() {
  int n; cin >> n;
  long long x=1, y=1;
  while (n--) {
    int a, b; cin >> a >> b;
    long long m = max((x+a-1)/a, (y+b-1)/b);
    x = a*m, y = b*m;
  }
  cout << x+y << '\n';
}
void d() {
  string s; cin >> s;
  int p = 0;
  for (const char& c : s) p += c=='p';
  cout << s.size()/2-p << '\n';
}
}

namespace ABC047 {
void a() {
  int n = 3;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  cout << (a[0]+a[1]==a[2] ? "Yes" : "No") << '\n';
}
void b() {
  int w, h, n; cin >> w >> h >> n;
  int l=0,r=w,d=0,u=h;
  while (n--) {
    int x, y, a; cin >> x >> y >> a;
    switch (a) {
      case 1: l = max(l,x); break;
      case 2: r = min(r,x); break;
      case 3: d = max(d,y); break;
      case 4: u = min(u,y); break;
    }
  }
  cout << max(0,r-l)*max(0,u-d) << '\n';
}
void c() {
  string s; cin >> s; int n = (int)s.size();
  int c = 0;
  for (int i = 0; i < n-1; i++) c += s[i]!=s[i+1];
  cout << c << '\n';
}
void d() {
  int n, t; cin >> n >> t;
  int mn=numeric_limits<int>::max(), mx=1, c=0;
  while (n--) {
    int a; cin >> a;
    mn = min(mn, a);
    if (a-mn == mx) {
      c++;
    } else if (a-mn > mx) {
      c = 1, mx = a-mn;
    }
  }
  cout << c << '\n';
}
}

namespace ABC048 {
void a() {
  string t = "";
  int n = 3;
  while (n--) {
    string s; cin >> s;
    t += toupper(s.front());
  }
  cout << t << '\n';
}
void b() {
  long long a, b, x; cin >> a >> b >> x;
  auto f = [&](long long n) {return n==-1 ? -1 : n/x;};
  cout << f(b)-f(a-1) << '\n';
}
void c() {
  int n, x; cin >> n >> x;
  long long c = 0;
  vector<int> a(n+1); for (int i = 0; i < n; i++) cin >> a[i+1];
  for (int i = 1; i < n+1; i++) {
    long long d = a[i-1]+a[i] - x;
    if (d > 0) {c += d; a[i] -= d;}
  }
  cout << c << '\n';
}
void d() {
  string s; cin >> s; int n = (int)s.size();
  cout << ((s.front()==s.back())^(n&1) ? "First" : "Second") << '\n';
}
}

namespace ABC049 {
void a() {
  set<char> vowels; for (const char& c : "aeiou"s) {vowels.insert(c);}
  char c; cin >> c;
  cout << (vowels.count(c) ? "vowel" : "consonant") << '\n';
}
void b() {
  int h, w; cin >> h >> w;
  while (h--) {
    string s; cin >> s;
    for (int i = 0; i < 2; i++) {
      cout << s << '\n';
    }
  }
}
void c() {
  string s; cin >> s;
  while (!s.empty()) {
    if (s.substr(s.size()-5,5)=="erase" || s.substr(s.size()-5,5)=="dream") {
      s.erase(s.size()-5,5); continue;
    } else if (s.substr(s.size()-6,6)=="eraser") {
      s.erase(s.size()-6,6); continue;
    } else if (s.substr(s.size()-7,7)=="dreamer") {
      s.erase(s.size()-7,7); continue;
    }
    cout << "NO" << '\n'; return;
  }
  cout << "YES" << '\n';
}
void d() {
  int n, k, l; cin >> n >> k >> l;
  UnionFind uf1(n), uf2(n);
  while (k--) {
    int p, q; cin >> p >> q; p--; q--;
    uf1.unite(p, q);
  }
  while (l--) {
    int r, s; cin >> r >> s; r--; s--;
    uf2.unite(r, s);
  }
  using P = pair<int, int>;
  map<P, int> c;
  for (int i = 0; i < n; i++) {
    c[P(uf1.find(i), uf2.find(i))]++;
  }
  for (int i = 0; i < n; i++) {
    cout << c[P(uf1.find(i), uf2.find(i))] << (i<n-1 ? ' ' : '\n');
  }

}
}

namespace ABC179 {
void a() {
}
void b() {

}
void c() {

}
void d() {
  int n, k; cin >> n >> k;
  vector<int> l(k), r(k);
  for (int i = 0; i < k; i++) cin >> l[i] >> r[i];
  vector<Mint> s(2*n); s[0] = 1; s[1] = -1;
  for (int i = 0; i < n-1; i++) {
    s[i+1] += s[i];
    for (int j = 0; j < k; j++) {
      s[i+l[j]] += s[i];
      s[i+r[j]+1] -= s[i];
    }
  }
  cout << s[n-1] << '\n';
}
void e() {
  long long n, x, m; cin >> n >> x >> m;
  vector<int> res(m, -1);
  long long s = 0;
  vector<int> loop(m+1);
  for (int i = 0; i < m+1; i++) {
    if (i==n) {cout << s << '\n'; return;}
    if (res[x] != -1) {
      int l = i-res[x];
      loop = vector<int>(loop.begin()+res[x], loop.begin()+i);
      long long c = 0; for (const int& v : loop) c += v;
      s += (n-i)/l*c;
      for (int j = 0; j < (n-i)%l; j++) s += loop[j];
      cout << s << '\n'; return;
    }
    res[x] = i, loop[i] = x;
    s += x; x = x*x%m;
  }
}
}


namespace ABC180 {
void a() {
  int n, a, b; cin >> n >> a >> b;
  cout << n-a+b << '\n';
}
void b() {
  int n; cin >> n;
  vector<long long> x(n);
  for (int i = 0; i < n; i++) {cin >> x[i]; x[i] = abs(x[i]);}
  cout << accumulate(x.begin(), x.end(), 0LL) << '\n';
  cout << setprecision(16) << sqrt(accumulate(x.begin(), x.end(), 0LL, [](long long &a, long long &b){return a+b*b;})) << '\n';
  cout << *max_element(x.begin(), x.end()) << '\n';

}
void c() {
  long long n; cin >> n;
  for (const auto& d : find_divisors(n)) cout << d << '\n';
}
void d() {
  long long x, y, a, b; cin >> x >> y >> a >> b;
  long long cnt = 0;
  while (1) {if (y/a<x || x*a >=y || x*a > x+b) {break;}; x *= a; cnt++;}
  cout << cnt+(y-x-1)/b << '\n';
}
void e() {
  int n; cin >> n;
  vector<int> x(n), y(n), z(n);
  for (int i = 0; i < n; i++) {
    cin >> x[i] >> y[i] >> z[i];
  }
  vector<vector<int>> dist(n, vector<int>(n, 0));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      dist[i][j] = abs(x[j]-x[i]) + abs(y[j]-y[i]) + max(0, z[j]-z[i]);
    }
  }
  int inf = numeric_limits<int>::max()/10;
  vector<vector<int>> dp(1<<n, vector<int>(n, inf));
  dp[0][0] = 0;
  for (int s = 0; s < (1<<n); s++) {
    for (int i = 0; i < n; i++) {
      for (int t=s|1<<i, j=0; j < n; j++) dp[t][i] = min(dp[t][i], dp[s][j]+dist[j][i]);
    }
  }
  cout << dp.back()[0] << '\n';

}
static void f() {
  int n, m, l; cin >> n >> m >> l;
  make_fact(n);
  vector<Mint> path(n+1, 0), cycle(n+1, 0);
  path[1] = path[2] = 1;
  for (int i = 3; i < n+1; i++) path[i] = path[i-1]*i;
  for (int i = 2; i < n+1; i++) cycle[i] = path[i-1];

  auto f = [&](int l) {
    vector<vector<Mint>> dp(n+1, vector<Mint>(m+1, 0)); dp[0][0] = 1;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m+1; j++) {
        for (int k = 1; k <= min({l, n-i, m-j+1}); k++) {
          dp[i+k][j+k-1] += dp[i][j]*choose_mod(n-i-1, k-1)*path[k];
        }
        for (int k = 2; k <= min({l, n-i, m-j}); k++) {
          dp[i+k][j+k] += dp[i][j]*choose_mod(n-i-1, k-1)*cycle[k];
        }
      }
    }
    return dp[n][m];
  };
  cout << f(l)-f(l-1) << '\n';
}
}

namespace ABC181 {
void a() {
  int n; cin >> n;
  cout << (n&1 ? "Black" : "White") << '\n';
}
void b() {
  int n; cin >> n;
  long long tot = 0;
  while (n--) {
    long long a, b; cin >> a >> b;
    tot += (a+b)*(b-a+1)/2;
  }
  cout << tot << '\n';
}
void c() {
  int n; cin >> n;
  vector<int> x(n), y(n);
  for (int i = 0; i < n; i++) {cin >> x[i] >> y[i];}
  vector<int> p(n);
  for (int i = 0; i < n; i++) {p[i] = i;}
  for (int i = 0; i < n; i++) {
    for (int j = i+1; j < n; j++) {
      for (int k = j+1; k < n; k++) {
        if ((x[j]-x[i])*(y[k]-y[j])!=(x[k]-x[j])*(y[j]-y[i])) {continue;}
        cout << "Yes" << '\n';
        return;
      }
    }
  }
  cout << "No" << '\n';
}
void d() {
  string s; cin >> s;
  if (s.size() < 3) {
    int bl = 0;
    if (stoi(s)%8==0) {bl = 1;}
    reverse(s.begin(), s.end());
    if (stoi(s)%8==0) {bl = 1;}
    cout << (bl ? "Yes" : "No") << '\n';
    return;
  }
  auto counter = [](const string& s) {
    vector<int> cnt(10);
    for (const char& c: s) {cnt[c-'0']++;}
    return cnt;
  };
  vector<int> sc(10);
  for (const char& c: s) {sc[c-'0']++;}
  for (int i = 112; i < 1000; i += 8) {
    auto c = sc;
    for (const char& d: to_string(i)) {c[d-'0']--;}
    if (all_of(c.begin(), c.end(), [&](int x){return x>=0;})) {
      cout << "Yes" << "\n"; return;
    }
  }
  cout << "No" << '\n';
}
void e() {
  int n, m; cin >> n >> m;
  vector<long long> h(n), w(m);
  for (int i = 0; i < n; i++) cin >> h[i];
  for (int i = 0; i < m; i++) cin >> w[i];
  sort(h.begin(), h.end());
  sort(w.begin(), w.end());
  vector<long long> l(n), r(n);
  for (int i = 1; i < n-1; i+=2) {l[i] = h[i]-h[i-1];}
  for (int i = n-2; i > 0; i-=2) {r[i] = h[i+1]-h[i];}
  for (int i = 0; i < n-1; i++) {l[i+1] += l[i];}
  for (int i = n-1; i > 0; i--) {r[i-1] += r[i];}
  vector<long long> d(n);
  for (int i = 1; i < n-1; i+=2) {d[i] = h[i+1]-h[i-1];}
  int k = 0;
  long long mn = numeric_limits<long long>::max();
  for (int i = 0; i < n; i++) {
    while (k < m-1 && abs(w[k+1]-h[i]) <= abs(w[k]-h[i])) ++k;
    mn = min(mn, l[max(i-1,0)]+r[min(i+1,n-1)]+d[i]+abs(w[k]-h[i]));
  }
  cout << mn << '\n';
}
void f() {
  int n; cin >> n;
  vector<int> x(n), y(n);
  for (int i = 0; i < n; i++) cin >> x[i] >> y[i];

  auto dist = [&](int i, int j) {
    int dx = x[j]-x[i], dy = y[j]-y[i];
    return dx*dx + dy*dy;
  };

  auto ok = [&](double r) {
    r *= 2;
    auto uf = UnionFind(n+2);
    for (int i = 0; i < n; i++) {
      if (100-y[i] < r) uf.unite(i, n);
      if (y[i]+100 < r) uf.unite(i, n+1);
    }
    for (int i = 0; i < n; i++) {
      for (int j = i+1; j < n; j++) {
        if (dist(i, j) < r*r) uf.unite(i,j);
      }
    }
    return !uf.same(n, n+1);
  };

  double lo = 0, hi = 100.1;
  for (int i = 0; i < 100; i++) {
    double r = (lo+hi)/2;
    if (ok(r)) {lo = r;} else {hi = r;}
  }
  cout << setprecision(10) << lo << '\n';

}
}

namespace ABC183 {
void a() {
  int x; cin >> x;
  cout << max(x,0) << '\n';
}
void b() {
  double sx, sy, gx, gy; cin >> sx >> sy >> gx >> gy;
  cout << setprecision(10) << (sx*gy+sy*gx)/(sy+gy) << '\n';
}
void c() {
 int n, k; cin >> n >> k;
 vector<vector<int>> t(n, vector<int>(n));
 for (int i = 0; i < n; i++) {
   for (int j = 0; j < n; j++) {
     cin >> t[i][j];
   }
 }
 vector<int> p(n-1);
 for (int i = 0; i < n-1; i++) {p[i] = i+1;}
 int tot = 0;
 do {
   int d = t[0][p[0]];
   for (int i = 0; i < n-2; i++) {d += t[p[i]][p[i+1]];}
   d += t[p[n-2]][0];
   tot += d==k;
 } while (next_permutation(p.begin(), p.end()));
 cout << tot << '\n';
}
void d() {
  int n, w; cin >> n >> w;
  int m = (int)2e5 + 10;
  vector<long long> a(m);
  while (n--) {
    int s, t, p; cin >> s >> t >> p;
    a[s] += p; a[t] -= p;
  }
  for (int i = 0; i < m-1; i++) {
    if (a[i]>w) {cout << "No" << '\n'; return;}
    a[i+1] += a[i];
  }
  cout << "Yes" << '\n';
}
void e() {
  int h, w; cin >> h >> w;
  vector<string> s(h);
  for (int i = 0; i < h; i++) {
    cin >> s[i];
  }
  vector<vector<long long>> x(h, vector<long long>(w, 0));
  vector<vector<long long>> y(h, vector<long long>(w, 0));
  vector<vector<long long>> z(h, vector<long long>(w, 0));
  vector<vector<long long>> c(h, vector<long long>(w, 0)); c[0][0] = 1;
  for (int i = 0; i < h; i++) {
    for (int j = 0; j < w; j++) {
      if (s[i][j] == '#') {continue;}
      if (i==0 && j==0) {continue;}
      if (i>0) {y[i][j] = (y[i-1][j]+c[i-1][j])%MOD;}
      if (j>0) {x[i][j] = (x[i][j-1]+c[i][j-1])%MOD;}
      if (i>0&&j>0) {z[i][j] = (z[i-1][j-1]+c[i-1][j-1])%MOD;}
      c[i][j] = (x[i][j]+y[i][j]+z[i][j])%MOD;
    }
  }
  cout << c[h-1][w-1] << '\n';
}
void f() {
  int n, q; cin >> n >> q;
  vector<map<int, int>> c(n);
  for (int i = 0; i < n; i++) {
    int x; cin >> x; --x;
    c[i][x] = 1;
  }
  auto uf = UnionFind(n);
  while (q--) {
    int t, x, y; cin >> t >> x >> y; --x; --y;
    x = uf.find(x);
    if (t==1) {
      y = uf.find(y);
      if (x==y) {continue;}
      if (uf.rank[x] < uf.rank[y]) {swap(x, y);}
      for (pair<int, int> const &p : c[y]) {
        c[x][p.first] += p.second;
      }
      uf.unite(x,y);
    } else {
      cout << c[x][y] << '\n';
    }
  }

}

}


}



namespace Codeforces {
}

int main() {
  ios::sync_with_stdio(false); cin.tie(0);


  AtCoder::ABC049::d();




  return 0;
}
