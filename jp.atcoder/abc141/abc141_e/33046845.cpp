#include <bits/stdc++.h>
using namespace std;
#define range(i, n) for(int i = 0; i < n; ++i)
#define range_rev(i, n) for(int i = n - 1; i >= 0; --i)
#define repeat(t) for(int __ = 0; __ < t; ++__)
#define iter(x, a) for(auto&& x: a)
template<typename T> using vec = vector<T>;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  string s;
  cin >> n >> s;
  vec<int> dp(n + 1);
  int mx = 0;
  range(i, n) range_rev(j, n) {
    dp[j + 1] = s[i] == s[j] ? dp[j] + 1 : 0;
    mx = max(mx, min(i - j, dp[j + 1]));
  }
  cout << mx << endl;
}
