#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 200;
  vector<vector<int>> dp(n + 1, vector<int>(k));
  dp[0][0] = 1;
  auto compute_dp = [&]() -> pair<int, int> {
    for(int i = 0; i < n; i++) {
      dp[i + 1] = dp[i];
      for(int j = 0; j < k; j++) {
        int r = (j + a[i]) % k;
        dp[i + 1][r] += dp[i][j];
        if((r && dp[i + 1][r] >= 2) || dp[i + 1][0] > 2) { return {i + 1, r}; }
      }
    }
    return {-1, -1};
  };
  auto [i0, r] = compute_dp();
  if(i0 == -1) {
    cout << "No" << endl;
    return 0;
  }
  auto find = [&](int r, int c) -> int {
    for(int i = 0; i < n + 1; i++) {
      if(dp[i][r] == c) { return i; }
    }
    return -1;
  };
  vector<int> b1;
  vector<int> b2;
  // int c0 = dp[i0][r];
  int i1 = r == 0 ? find(r, 2) : find(r, 1);
  int i = i0;
  int r0 = r;
  while(i > 0) {
    i--;
    if(dp[i + 1][r] - dp[i][r] > 0) {
      b1.push_back(i);
      r = ((r - a[i]) % k + k) % k;
    }
    if(r == 0) break;
  };
  i = i1;
  r = r0;
  while(i > 0) {
    i--;
    if(dp[i + 1][r] - dp[i][r] > 0) {
      b2.push_back(i);
      r = ((r - a[i]) % k + k) % k;
    }
    if(r == 0) break;
  };
  reverse(b1.begin(), b1.end());
  reverse(b2.begin(), b2.end());
  cout << "Yes" << endl;
  cout << b1.size() << ' ';
  for(int i = 0; i < (int)b1.size(); i++) {
    cout << b1[i] + 1 << " \n"[i == (int)b1.size() - 1];
  }
  cout << b2.size() << ' ';
  for(int i = 0; i < (int)b2.size(); i++) {
    cout << b2[i] + 1 << " \n"[i == (int)b2.size() - 1];
  }
}
