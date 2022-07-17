#include <bits/stdc++.h>
using namespace std;
struct union_find {
  vector<int> data;
  union_find(int size): data(size, -1) {}
  auto root(int u) -> int { return data[u] < 0 ? u : data[u] = root(data[u]); }
  auto unite(int u, int v) {
    u = root(u), v = root(v);
    if(u == v) return;
    if(data[u] > data[v]) swap(u, v);
    data[u] += data[v];
    data[v] = u;
  }
  auto size_of(int u) -> int { return -data[root(u)]; }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, x, y, z;
  cin >> n >> x >> y >> z;
  vector<int> a(n);
  vector<int> b(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  vector<int> res;
  vector<bool> passed(n);
  vector<int> id(n);
  iota(id.begin(), id.end(), 0);
  sort(id.begin(), id.end(), [&](int i, int j) {
    return a[i] != a[j] ? a[i] > a[j] : i < j;
  });
  // for(int i = 0; i < n; i++) cout << id[i] << " \n"[i == n - 1];
  // cout << x << ' ' << y << ' ' << z << endl;
  int cnt = 0;
  for(int i = 0; i < n; i++) {
    if(cnt == x) break;
    if(passed[id[i]]) continue;
    res.push_back(id[i]);
    passed[id[i]] = true;
    cnt++;
  }
  sort(id.begin(), id.end(), [&](int i, int j) {
    return b[i] != b[j] ? b[i] > b[j] : i < j;
  });
  cnt = 0;
  for(int i = 0; i < n; i++) {
    if(cnt == y) break;
    if(passed[id[i]]) continue;
    res.push_back(id[i]);
    passed[id[i]] = true;
    cnt++;
  }
  sort(id.begin(), id.end(), [&](int i, int j) {
    return a[i] + b[i] != a[j] + b[j] ? a[i] + b[i] > a[j] + b[j] : i < j;
  });
  cnt = 0;
  for(int i = 0; i < n; i++) {
    if(cnt == z) break;
    if(passed[id[i]]) continue;
    res.push_back(id[i]);
    passed[id[i]] = true;
    cnt++;
  }
  sort(res.begin(), res.end());
  for(int i: res) cout << i + 1 << endl;
}
