#include <bits/stdc++.h>
using namespace std;
template<typename T> class median_queue {
  using Self = median_queue;
  multiset<T> lo, hi;
  auto balance() -> int { return (int)lo.size() - (int)hi.size(); }
  auto rebalance() {
    int b = balance();
    if(b == 2) {
      auto p = --lo.end();
      hi.insert(*p);
      lo.erase(p);
    } else if(b == -1) {
      auto p = hi.begin();
      lo.insert(*p);
      hi.erase(p);
    }
  }

public:
  median_queue() = default;
  auto size() -> int { return lo.size() + hi.size(); }
  auto insert(T x) {
    if(balance() == 1) lo.insert(x);
    else hi.insert(x);
    rebalance();
  }
  auto low() -> T { return *lo.rbegin(); }
  auto high() -> T { return balance() == 1 ? *lo.rbegin() : *hi.begin(); }
  auto remove(T x) {
    auto p = lo.find(x);
    if(p != lo.end()) lo.erase(p);
    else hi.erase(hi.find(x));
    rebalance();
  }
};
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<vector<int>> g(n);
  for(int i = 0; i < n - 1; i++) {
    int u, v;
    cin >> u >> v;
    u--;
    v--;
    g[u].push_back(v);
    g[v].push_back(u);
  }
  function<int(int, int, int)> dfs;
  median_queue<int> que;
  dfs = [&](int u, int p, int turn) -> int {
    que.insert(a[u]);
    vector<int> cand;
    for(auto& v: g[u]) {
      if(v == p) continue;
      cand.push_back(dfs(v, u, turn ^ 1));
    }
    sort(cand.begin(), cand.end());
    if(turn == 0) reverse(cand.begin(), cand.end());
    int res;
    if(cand.size()) res = cand.front();
    else res = (que.low() + que.high()) >> 1;
    que.remove(a[u]);
    return res;
  };
  cout << dfs(0, -1, 0) << endl;
}
