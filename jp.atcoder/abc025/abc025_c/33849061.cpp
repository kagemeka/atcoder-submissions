#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int const n = 9;
  vector<int> b(n), c(n);
  for(int i = 0; i < 6; i++) cin >> b[i];
  for(int i = 0; i < n; i++) {
    if(i % 3 != 2) cin >> c[i];
  }
  int tot = 0;
  for(int i = 0; i < n; i++) tot += b[i] + c[i];
  function<int(int, int)> dfs;
  using pi = pair<int, int>;
  map<pi, int> cache;
  auto compute_first_score = [&](int state) -> int {
    int s = 0;
    for(int i = 0; i < 6; i++) {
      s += ((state >> i & 1) == (state >> (i + 3) & 1)) * b[i];
    }
    for(int i = 0; i < n; i++) {
      if(i % 3 == 2) continue;
      s += ((state >> i & 1) == (state >> (i + 1) & 1)) * c[i];
    }
    return s;
  };
  dfs = [&](int is_set, int state) -> int {
    pi node = {is_set, state};
    if(cache.count(node)) { return cache[node]; }
    int c = __builtin_popcount(is_set);
    if(c == n) { return cache[node] = compute_first_score(state); }
    int turn = c & 1;
    vector<int> cand;
    for(int i = 0; i < n; i++) {
      if(is_set >> i & 1) continue;
      cand.push_back(dfs(is_set | (1 << i), state | ((1 << i) * turn)));
    }
    sort(cand.begin(), cand.end());
    int m = cand.size();
    return cache[node] = (turn == 0 ? cand[m - 1] : cand[0]);
  };
  int a = dfs(0, 0);
  cout << a << ' ' << tot - a << endl;
}
