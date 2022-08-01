#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  using pi = pair<int, int>;
  vector<pi> chocolates(n), boxes(m);
  for(int i = 0; i < n; i++) cin >> chocolates[i].first;
  for(int i = 0; i < n; i++) cin >> chocolates[i].second;
  for(int i = 0; i < m; i++) cin >> boxes[i].first;
  for(int i = 0; i < m; i++) cin >> boxes[i].second;
  sort(chocolates.begin(), chocolates.end());
  sort(boxes.begin(), boxes.end());
  multiset<int> s;
  for(int i = 0, j = 0; i < m; i++) {
    auto [x, y] = boxes[i];
    while(j < n && chocolates[j].first <= x) {
      s.insert(chocolates[j].second);
      j++;
    }
    auto it = s.upper_bound(y);
    if(it == s.begin()) continue;
    s.erase(--it);
  }
  cout << (s.size() ? "No" : "Yes") << endl;
}
