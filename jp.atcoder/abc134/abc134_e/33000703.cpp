#include <bits/stdc++.h>
using namespace std;

template<typename T, typename A>
auto longest_non_decreasing_subsequence(const T& inf, const A& a) -> vector<T> {
  int n = a.size();
  vector<T> dp(n, inf);
  for(auto& x: a) {
    int i = upper_bound(dp.begin(), dp.end(), x) - dp.begin();
    dp[i] = x;
  }
  return vector(dp.begin(), lower_bound(dp.begin(), dp.end(), inf));
}

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];

  int const inf = 1 << 30;

  reverse(a.begin(), a.end());
  auto lnds = longest_non_decreasing_subsequence(inf, a);
  cout << lnds.size() << endl;
}
