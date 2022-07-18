#include <bits/stdc++.h>
using namespace std;
template<typename T, class F = function<T(const T&, const T&)>>
class sparse_table {
public:
  vector<vector<T>> data;
  F f;
  sparse_table(vector<T> const& a, const F& f): f(f) {
    int n = a.size();
    if(!n) return;
    int height = 32 - __builtin_clz(n);
    data.resize(height);
    data[0] = a;
    for(int i = 1; i < height; i++) {
      int w = n - (1 << i) + 1;
      data[i].resize(w);
      for(int j = 0; j < w; j++) {
        data[i][j] = f(data[i - 1][j], data[i - 1][j + (1 << (i - 1))]);
      }
    }
  }
  auto size() -> int { return data[0].size(); }
  auto get(int l, int r) -> T {
    assert(0 <= l && l < r && r <= size());
    if(r - l == 1) return data[0][l];
    int i = 32 - __builtin_clz(r - l + 1) - 1;
    return f(data[i][l], data[i][r - (1 << i) + 1]);
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  cin >> n >> q;
  vector<long> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  vector<long> da(n - 1), db(n - 1);
  for(int i = 0; i < n - 1; i++) da[i] = abs(a[i + 1] - a[i]);
  for(int i = 0; i < n - 1; i++) db[i] = abs(b[i + 1] - b[i]);
  auto f = [&](long x, long y) { return gcd(x, y); };
  sparse_table spa(da, f);
  sparse_table spb(db, f);
  while(q--) {
    int h0, h1, w0, w1;
    cin >> h0 >> h1 >> w0 >> w1;
    h0--;
    h1--;
    w0--;
    w1--;
    long ga = h0 < h1 ? spa.get(h0, h1) : 0;
    long gb = w0 < w1 ? spb.get(w0, w1) : 0;
    cout << abs(gcd(a[h0] + b[w0], gcd(ga, gb))) << endl;
  }
}
