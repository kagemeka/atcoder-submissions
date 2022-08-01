#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  using pi = pair<int, int>;
  vector<pi> items(m);
  for(int i = 0; i < m; i++) { cin >> items[i].second >> items[i].first; }
  sort(items.begin(), items.end());
  int g = n;
  long s = 0;
  for(auto& [c, a]: items) {
    int ng = gcd(g, a);
    s += (long)(g - ng) * c;
    g = ng;
  }
  cout << (g == 1 ? s : -1) << endl;
}
