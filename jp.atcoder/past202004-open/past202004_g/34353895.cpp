#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int q;
  cin >> q;
  queue<pair<char, int>> que;
  while(q--) {
    int t;
    cin >> t;
    if(t == 1) {
      char c;
      int x;
      cin >> c >> x;
      que.emplace(c, x);
    } else {
      vector<long> remove_cnt(26);
      long tot = 0;
      int d;
      cin >> d;
      while(que.size() && d) {
        auto& [c, x] = que.front();
        int v = min(x, d);
        x -= v;
        d -= v;
        remove_cnt[c - 'a'] += v;
        if(!x) que.pop();
      }
      for(auto& x: remove_cnt) { tot += x * x; }
      cout << tot << '\n';
    }
  }
}
