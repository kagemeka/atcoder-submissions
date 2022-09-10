#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  vector<string> s(n), t(m);
  for(int i = 0; i < n; i++) cin >> s[i];
  for(int i = 0; i < m; i++) cin >> t[i];
  // 3 <= |x| <= 16
  int l_sum = 0;
  for(auto& s: s) l_sum += s.size();
  int hi = 16 - l_sum - (n - 1);
  int lo = max(0, 3 - l_sum - (n - 1));
  assert(hi >= 0);
  set<string> st;
  for(auto& t: t) st.insert(t);
  auto make = [&](vector<string> s, vector<int> a) -> string {
    string x = "";
    for(int i = 0; i < n; i++) {
      x += s[i];
      if(i < n - 1) { x += string(a[i] + 1, '_'); }
    }
    assert(3 <= x.size() && x.size() <= 16);
    return x;
  };
  auto contains = [&](string s) -> bool { return st.count(s); };
  auto f = [&](vector<string> s) {
    queue<pair<vector<int>, int>> que;
    que.emplace(vector<int>(n - 1), 0);
    while(que.size()) {
      auto [a, k] = que.front();
      que.pop();
      if(k >= lo) {
        string x = make(s, a);
        // cout << x << endl;
        if(!contains(x)) {
          cout << x << endl;
          return true;
        }
      }
      if(k == hi) { continue; }
      for(int i = 0; i < n - 1; i++) {
        auto b = a;
        b[i] += 1;
        que.emplace(b, k + 1);
      }
    }
    return false;
  };
  vector<int> idx(n);
  iota(idx.begin(), idx.end(), 0);
  do {
    vector<string> w(n);
    for(int i = 0; i < n; i++) w[i] = s[idx[i]];
    if(f(w)) return 0;
    // for(int i = 0; i < n; i++) cout << s[i] << " \n"[i == n - 1];
  } while(next_permutation(idx.begin(), idx.end()));
  cout << -1 << endl;
}
