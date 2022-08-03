#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int q;
  cin >> q;
  vector<int> res(q);
  using tup = tuple<int, int, int>;
  vector<tup> events;
  for(int i = 0; i < n; i++) { events.emplace_back(i, 1, a[i]); }
  vector<int> qx(q);
  for(int i = 0; i < q; i++) {
    int l, r, x;
    cin >> l >> r >> x;
    qx[i] = x;
    l--;
    r--;
    events.emplace_back(l, 0, i);
    events.emplace_back(r + 1, 0, i);
  }
  sort(events.begin(), events.end());
  vector<int> count(n + 1);
  for(auto& [i, t, j]: events) {
    if(t == 1) {
      count[j]++;
      continue;
    }
    int x = qx[j];
    res[j] = count[x] - res[j];
  }
  for(auto& x: res) { cout << x << endl; }
}
