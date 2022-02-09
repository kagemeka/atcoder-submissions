#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, a;
  cin >> n >> a;
  vector<int> x(n);
  for (int i = 0; i < n; i++) cin >> x[i];
  for (int i = 0; i < n; i++) x[i] -= a;
  unordered_map<int, long long> dp;
  dp[0] = 1;
  for (int i = 0; i < n; i++) {
    auto ndp = dp;
    for (auto kv : dp) {
      int k = kv.first;
      int v = kv.second;
      if (ndp.find(k+x[i]) != ndp.end()) {
        ndp[k+x[i]] += v;
      } else {
        ndp[k+x[i]] = v;
      }
    }
    dp = ndp;
  }
  cout << dp[0] - 1 << '\n';
  return 0;
}
