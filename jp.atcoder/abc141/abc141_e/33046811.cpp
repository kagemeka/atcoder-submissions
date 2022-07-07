#include <bits/stdc++.h>
using namespace std;
#define range(i, n) for(int i = 0; i < n; ++i)
#define range_rev(i, n) for(int i = n - 1; i >= 0; --i)
#define repeat(t) for(int __ = 0; __ < t; ++__)
#define iter(x, a) for(auto&& x: a)
template<typename T> using vec = vector<T>;
template<typename A> auto lc_substr_dp(const A& a, const A& b)
  -> vec<vec<int>> {
  int n = a.size(), m = b.size();
  vec<vec<int>> dp(n + 1, vec<int>(m + 1));
  range(i, n) range(j, m) dp[i + 1][j + 1] = a[i] == a[j] ? dp[i][j] + 1 : 0;
  return dp;
}
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  string s;
  cin >> n >> s;
  auto dp = lc_substr_dp(s, s);
  int mx = 0;
  range(i, n) range(j, i) mx = max(mx, min(i - j, dp[i + 1][j + 1]));
  cout << mx << endl;
}
