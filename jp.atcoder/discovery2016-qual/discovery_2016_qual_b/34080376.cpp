#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 1 << 17;
  vector<vector<int>> indices(k);
  for(int i = 0; i < n; i++) { indices[a[i]].push_back(i); }
  vector<vector<int>> b;
  for(int i = 0; i < k; i++) {
    if(indices[i].empty()) continue;
    b.emplace_back(indices[i]);
  }
  int x = -1;
  int cnt = 1;
  for(auto& indices: b) {
    auto it = upper_bound(indices.begin(), indices.end(), x);
    if(it == indices.begin()) {
      x = *(indices.end() - 1);
    } else {
      cnt++;
      x = *(it - 1);
    }
  }
  if(x == 0) { cnt--; }
  cout << cnt << '\n';
}
