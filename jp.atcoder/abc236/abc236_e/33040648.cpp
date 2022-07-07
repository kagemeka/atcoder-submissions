
#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  {
    // average
    // >= possible?
    auto possible = [&](double x) -> bool {
      vector<double> dp(2);
      for(int i = 0; i < n; i++) {
        auto b = a[i] - x;
        vector<double> ndp(2);
        ndp[0] = dp[1];
        ndp[1] = max(dp[0], dp[1]) + b;
        swap(dp, ndp);
      }
      return max(dp[0], dp[1]) >= 0;
    };
    double ok = 0, ng = 1 << 30;
    for(int i = 0; i < 100; i++) {
      auto x = (ok + ng) / 2;
      if(possible(x)) ok = x;
      else ng = x;
    }
    cout << setprecision(16) << ok << endl;
  }
  {
    // median
    auto possible = [&](int x) -> bool {
      vector<int> dp(2);
      for(int i = 0; i < n; i++) {
        auto b = a[i] >= x ? 1 : -1;
        vector<int> ndp(2);
        ndp[0] = dp[1];
        ndp[1] = max(dp[0], dp[1]) + b;
        swap(dp, ndp);
      }
      return max(dp[0], dp[1]) >= 0;
    };
    int ok = 0, ng = 1 << 30;
    while(ng - ok > 1) {
      auto x = (ok + ng) / 2;
      if(possible(x)) ok = x;
      else ng = x;
    }
    cout << ok << endl;
  }
}
