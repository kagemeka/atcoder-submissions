#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  unordered_map<string, int> res;
  for (int i = 0; i < n; i++) {
    string s; cin >> s;
    (res.find(s) != res.end()) ? res[s]++ : res[s] = 1;
  }
  int m = 0;
  for (auto &p : res) m = max(m, p.second);
  vector<string> ans;
  for (auto &p : res) {
    if (p.second < m) continue;
    ans.push_back(p.first);
  }
  sort(ans.begin(), ans.end());
  for (auto &s : ans) cout << s << '\n';
  return 0;
}
