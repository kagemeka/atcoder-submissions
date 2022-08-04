#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<int> p(n);
  for(int i = 0; i < n; i++) cin >> p[i];
  vector<int> root(n), cnt(n);
  for(int i = 0; i < n; i++) root[i] = i;
  vector<vector<int>> cards(n);
  set<int> st;
  vector<int> res(n, -1);
  for(int i = 0; i < n; i++) {
    int x = p[i] - 1;
    auto it = st.lower_bound(x);
    if(it != st.end()) {
      int y = *it;
      st.erase(it);
      root[x] = root[y];
    }
    int rx = root[x];
    cnt[rx]++;
    cards[rx].push_back(x);
    if(cnt[rx] == k) {
      while(cards[rx].size()) {
        int y = cards[rx].back();
        cards[rx].pop_back();
        res[y] = i + 1;
      }
    } else {
      st.insert(x);
    }
  }
  for(auto& x: res) cout << x << endl;
}
