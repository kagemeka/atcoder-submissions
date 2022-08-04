#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int k, n;
  cin >> k >> n;
  // 3^k * 50 * 27 = 2.5 ^10^7
  vector<pair<string, string>> vw(n);
  for(int i = 0; i < n; i++) cin >> vw[i].first >> vw[i].second;
  auto f = [&](vector<int> const& len) -> vector<string> {
    vector<string> s(k, "");
    for(auto& [v, w]: vw) {
      int i = 0;
      for(auto& c: v) {
        int d = c - '1';
        int l = len[d];
        if(s[d] != "") {
          if(w.substr(i, l) != s[d]) return {};
          i += l;
          continue;
        }
        string t = "";
        for(int j = 0; j < l; j++) {
          if(i >= (int)w.size()) return {};
          t += w[i];
          i++;
        }
        s[d] = t;
      }
      if(i != (int)w.size()) return {};
    }
    return s;
  };
  function<vector<string>(vector<int>&)> dfs;
  dfs = [&](vector<int>& len) -> vector<string> {
    if((int)len.size() == k) { return f(len); }
    for(int l = 1; l <= 3; l++) {
      len.push_back(l);
      auto res = dfs(len);
      if((int)res.size() == k) return res;
      len.pop_back();
    }
    return {};
  };
  vector<int> len = {};
  auto res = dfs(len);
  for(int i = 0; i < k; i++) { cout << res[i] << endl; }
}
