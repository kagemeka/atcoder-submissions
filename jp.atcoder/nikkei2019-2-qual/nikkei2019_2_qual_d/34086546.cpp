#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<vector<pair<int, int>>> a(n);
  while(m--) {
    int l, r, c;
    cin >> l >> r >> c;
    l--;
    r--;
    a[l].emplace_back(r, c);
  }
  long const inf = 1l << 60;
  vector<long> dist(n, inf);
  priority_queue<pair<long, int>> que;
  que.emplace(0, 0);
  for(int i = 0; i < n; i++) {
    while(que.size() && que.top().second < i) { que.pop(); }
    if(que.empty()) {
      cout << -1 << endl;
      return 0;
    }
    dist[i] = -que.top().first;
    for(auto& [r, c]: a[i]) { que.emplace(-(dist[i] + c), r); }
  }
  cout << dist[n - 1] << endl;
}
