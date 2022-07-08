#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  using p = pair<int, int>;
  vector<p> ab(n);
  for(int i = 0; i < n; i++) cin >> ab[i].first >> ab[i].second;
  sort(ab.begin(), ab.end());
  long cost = 0;
  for(auto& [a, b]: ab) {
    if(b >= m) {
      cost += (long)a * m;
      break;
    }
    cost += (long)a * b;
    m -= b;
  }
  cout << cost << endl;
}
