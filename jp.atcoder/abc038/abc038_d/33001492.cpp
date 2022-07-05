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
  using p = pair<int, int>;
  vector<p> wh;
  for(int i = 0; i < n; i++) {
    int w, h;
    cin >> w >> h;
    wh.emplace_back(w, h);
  }
  sort(wh.begin(), wh.end(), [](p a, p b) {
    if(a.first != b.first) return a.first < b.first;
    return a.second > b.second;
  });

  vector<int> a;
  for(auto& [w, h]: wh) { a.push_back(h); }
  int const inf = 1 << 30;
  cout << longest_increasing_subsequence(inf, a).size() << endl;
}
