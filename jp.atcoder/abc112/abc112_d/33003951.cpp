#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  vector<int> d;
  for(int i = 1; i * i <= m; i++) {
    if(m % i) continue;
    d.push_back(i);
    if(i * i != m) d.push_back(m / i);
  }

  sort(d.begin(), d.end());
  cout << m / *lower_bound(d.begin(), d.end(), n) << endl;
}
