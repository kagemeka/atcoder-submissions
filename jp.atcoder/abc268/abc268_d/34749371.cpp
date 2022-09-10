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
  set<string> st;
  for(auto& t: t) st.insert(t);
  auto make = [&](vector<string> s, vector<int> a) -> string {
    string x = "";
    for(int i = 0; i < n; i++) {
      x += s[i];
      if(i < n - 1) { x += string(a[i] + 1, '_'); }
    }
    return x;
  };
  auto contains = [&](string s) -> bool { return st.count(s); };
  auto f = [&](vector<string> s) {
    queue<pair<vector<int>, int>> que;
    que.emplace(vector<int>(n - 1), 0);
    while(que.size()) {
      auto [a, k] = que.front();
      que.pop();
      string x = make(s, a);
      if(!contains(x)) {
        cout << x << endl;
        return true;
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
  do {
    if(f(s)) return 0;
  } while(next_permutation(s.begin(), s.end()));
  cout << -1 << endl;
}
