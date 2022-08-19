#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, x;
  cin >> n >> x;
  vector<pair<int, int>> meals(n);
  for(int i = 0; i < n; i++) cin >> meals[i].first;
  for(int i = 0; i < n; i++) cin >> meals[i].second;
  int const k = 1 << 17;
  vector<vector<int>> values(k);
  for(auto& [t, a]: meals) { values[t].push_back(a); }
  auto possible = [&](int y) -> bool {
    priority_queue<int> que;
    long s = 0;
    int j = k - 1;
    for(int i = y - 1; i >= 0; i--) {
      while(j > i) {
        for(auto& v: values[j]) que.push(v);
        j--;
      }
      if(que.size()) {
        s += que.top();
        que.pop();
      }
    }
    return s >= x;
  };
  int ng = 0, ok = k;
  while(ok - ng > 1) {
    int y = (ok + ng) >> 1;
    if(possible(y)) ok = y;
    else ng = y;
  }
  cout << (ok < k ? ok : -1) << endl;
}
