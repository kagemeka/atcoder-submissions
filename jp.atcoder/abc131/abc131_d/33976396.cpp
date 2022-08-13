#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  using pi = pair<int, int>;
  vector<pi> ab(n);
  for(int i = 0; i < n; i++) cin >> ab[i].second >> ab[i].first;
  sort(ab.begin(), ab.end());
  long t = 0;
  for(auto& [b, a]: ab) {
    if(t > b - a) {
      cout << "No" << endl;
      return 0;
    }
    t += a;
  }
  cout << "Yes" << endl;
}
