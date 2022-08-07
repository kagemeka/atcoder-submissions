#include <bits/stdc++.h>
using namespace std;
struct fenwick {
  vector<int> data;
  fenwick(int size): data(size + 1) {}
  auto size() -> int { return data.size() - 1; }
  auto add(int i, int x) {
    for(++i; i <= size(); i += i & -i) data[i] += x;
  }
  auto get(int i) -> int {
    int v = 0;
    for(; i > 0; i -= i & -i) v += data[i];
    return v;
  }
};
auto main() -> int {
  int n;
  cin >> n;
  vector<int> c(n), a(n);
  for(int i = 0; i < n; i++) cin >> c[i];
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<vector<int>> b(n + 1);
  for(int i = 0; i < n; i++) {
    b[c[i]].push_back(--a[i]);
    b[0].push_back(a[i]);
  }
  long s = 0;
  fenwick fw(n);
  for(int i = 0; i <= n; i++) {
    auto& x = b[i];
    int sign = (i == 0) ? 1 : -1;
    for(int j = (int)x.size(); j-- > 0;) {
      s += sign * fw.get(x[j]);
      fw.add(x[j], 1);
    }
    for(auto& x: x) fw.add(x, -1);
  }
  cout << s << endl;
}
