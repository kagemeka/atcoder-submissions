#include <bits/stdc++.h>
using namespace std;
auto solve() -> bool {
  int n;
  cin >> n;
  using p = pair<int, int>;
  vector<p> lr(n);
  for(int i = 0; i < n; i++) cin >> lr[i].first >> lr[i].second;
  sort(lr.begin(), lr.end());
  int j = 0;
  int x = 0;
  priority_queue<int, vector<int>, greater<>> que;
  while(j < n || que.size()) {
    if(!que.size()) { x = lr[j].first; }
    while(j < n && lr[j].first == x) {
      que.push(lr[j].second);
      j++;
    }
    int y = que.top();
    if(y < x) { return false; }
    que.pop();
    x++;
  }
  return true;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int t;
  cin >> t;
  while(t--) { cout << (solve() ? "Yes" : "No") << endl; }
}
