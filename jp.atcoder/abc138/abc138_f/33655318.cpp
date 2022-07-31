#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long l, r;
  cin >> l >> r;
  long const mod = 1000000007;
  struct dp_table {
    vector<long> dp;
    dp_table(): dp(8) {}
    auto operator[](tuple<int, int, int> idx) -> long& {
      int s = 0;
      auto [i, j, k] = idx;
      s |= (1 << 0) * i;
      s |= (1 << 1) * j;
      s |= (1 << 2) * k;
      return dp[s];
    }
  };
  dp_table dp;
  dp[{0, 0, 0}] = 1;
  for(int m = 60; m-- > 0;) {
    dp_table ndp;
    int lv = l >> m & 1;
    int rv = r >> m & 1;
    for(int i = 0; i < 2; i++) {
      for(int j = 0; j < 2; j++) {
        for(int k = 0; k < 2; k++) {
          long pre = dp[{i, j, k}];
          for(int x = 0; x < 2; x++) {
            for(int y = 0; y < 2; y++) {
              if(x && !y) continue;
              int ni = i, nj = j, nk = k;
              if(!k && x ^ y) continue;
              if(x & y) nk = 1;
              if(!i && !x && lv) continue;
              if(x && !lv) ni = 1;
              if(!j && y && !rv) continue;
              if(!y && rv) nj = 1;
              ndp[{ni, nj, nk}] += pre;
              ndp[{ni, nj, nk}] %= mod;
            }
          }
        }
      }
    }
    swap(dp, ndp);
  }
  long res = 0;
  for(int i = 0; i < 2; i++) {
    for(int j = 0; j < 2; j++) {
      for(int k = 0; k < 2; k++) {
        res += dp[{i, j, k}];
        res %= mod;
      }
    }
  }
  cout << res << endl;
}
