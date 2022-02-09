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

  unordered_set<int> res = {0};
  for (int i = 0; i < n; i++) {
    unordered_set<int> nxt;
    for (auto &x : res) {
      for (auto &y : t[i]) {
        nxt.insert(x ^ y);
      }
    }
    res = nxt;
  }
  string ans = (res.find(0) != res.end()) ? "Found" : "Nothing";
  cout << ans << '\n';
  return 0;
}
