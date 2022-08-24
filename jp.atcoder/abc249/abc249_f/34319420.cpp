#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, k;
  cin >> n >> k;
  vector<pair<int, int>> ty(n + 1);
  ty[0].first = 1;
  for(int i = 1; i < n + 1; i++) cin >> ty[i].first >> ty[i].second;
  reverse(ty.begin(), ty.end());
  long const inf = 1l << 60;
  long mx = -inf;
  long s = 0;
  priority_queue<int> que;
  for(auto& [t, y]: ty) {
    while(que.size() && k < 0) {
      k++;
      s += que.top();
      que.pop();
    }
    if(k < 0) { break; }
    if(t == 2) {
      if(y >= 0) {
        s += y;
        continue;
      }
      que.push(y);
      k--;
    }
    if(t == 1) {
      mx = max(mx, s + y);
      k--;
    }
  }
  cout << mx << endl;
}
