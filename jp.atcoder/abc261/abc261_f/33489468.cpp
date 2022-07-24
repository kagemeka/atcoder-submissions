#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<int> data;
  fenwick(int size): data(size + 1) {}
  auto size() -> int { return data.size() - 1; }
  auto add(int i, int x) {
    for(i++; i <= size(); i += i & -i) data[i] += x;
  }
  auto get(int i) -> int {
    int v = 0;
    for(; i > 0; i -= i & -i) v += data[i];
    return v;
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> c(n), x(n);
  for(int i = 0; i < n; i++) cin >> c[i];
  for(int i = 0; i < n; i++) cin >> x[i];
  vector<vector<int>> a(1 << 19);
  for(int i = 0; i < n; i++) {
    a[c[i]].push_back(x[i]);
    a[0].push_back(x[i]);
  }
  fenwick fw(1 << 19);
  long cnt = 0;
  for(int k = 0; k < 1 << 19; k++) {
    auto& x = a[k];
    int sign = k == 0 ? 1 : -1;
    for(int i = (int)x.size() - 1; i >= 0; i--) {
      cnt += sign * fw.get(x[i]);
      fw.add(x[i], 1);
    }
    for(auto& x: x) { fw.add(x, -1); }
  }
  cout << cnt << endl;
}
