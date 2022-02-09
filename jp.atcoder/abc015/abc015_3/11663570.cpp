#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  vector<vector<int>> t(n, vector<int>(k));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < k; j++) {
      cin >> t[i][j];
    }
  }
  unordered_set<int> res;
  vector<pair<int, int>> stack = {pair<int, int>(0, 0)};
  while (!stack.empty()) {
    auto node = stack.back(); stack.pop_back();
    auto x = node.first;
    auto rank = node.second;
    if (rank == n) {res.insert(x); continue;}
    for (auto y : t[rank]) {
      stack.push_back(pair<int, int>(x ^ y, rank + 1));
    }
  }
  string ans = (res.find(0) != res.end()) ? "Found" : "Nothing";
  cout << ans << '\n';
  return 0;
}
