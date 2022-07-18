#include <bits/stdc++.h>
using namespace std;
template<typename T, class F = function<T(const T&, const T&)>>
class sparse_table {
  auto bitlen(int n) -> int { return 32 - __builtin_clz(n); }

public:
  vector<vector<T>> data;
  F f;
  sparse_table(vector<T> const& a, const F& f): f(f) {
    int n = a.size();
    if(!n) return;
    int height = bitlen(n - 1);
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
    int i = bitlen(r - l - 1) - 1;
    return f(data[i][l], data[i][r - (1 << i)]);
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, q;
  cin >> n >> q;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  vector<int> da(n - 1), db(n - 1);
  for(int i = 0; i < n - 1; i++) da[i] = a[i + 1] - a[i];
  for(int i = 0; i < n - 1; i++) db[i] = b[i + 1] - b[i];
  auto f = [&](int x, int y) { return gcd(x, y); };
  sparse_table spa(da, f);
  sparse_table spb(db, f);
  while(q--) {
    int h0, h1, w0, w1;
    cin >> h0 >> h1 >> w0 >> w1;
    h0--;
    h1--;
    w0--;
    w1--;
    int ga = h0 < h1 ? spa.get(h0, h1) : 0;
    int gb = w0 < w1 ? spb.get(w0, w1) : 0;
    cout << abs(gcd(a[h0] + b[w0], gcd(ga, gb))) << endl;
  }
}
