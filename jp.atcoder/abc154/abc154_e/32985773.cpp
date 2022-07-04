					#include <bits/stdc++.h>

using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string s;
  int k;
  cin >> s >> k;

  vector<int> dp0(4), dp1(4);
  dp0[0] = 1;
  for (auto& c : s) {
    int d = c - '0';
    for (int j = 2; j >= 0; j--) {
      dp1[j + 1] += dp1[j] * 9;
    }
    if (d > 0) {
      for (int j = 0; j < 4; j++) {
        dp1[j] += dp0[j];
      }
      for (int j = 2; j >= 0; j--) {
        dp1[j + 1] += dp0[j] * (d - 1);
        dp0[j + 1] = dp0[j];
        dp0[j] = 0;
      }
    }
  }
  cout << dp0[k] + dp1[k] << endl;
}
