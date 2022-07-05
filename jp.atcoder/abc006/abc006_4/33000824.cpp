#include <bits/stdc++.h>
using namespace std;

template<typename T, typename A>
auto longest_increasing_subsequence(const T& inf, const A& a) -> vector<T> {
  int n = a.size();
  vector<T> dp(n, inf);
  for(auto& x: a) *lower_bound(dp.begin(), dp.end(), x) = x;
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

  cout << n - longest_increasing_subsequence(inf, a).size() << endl;
}
