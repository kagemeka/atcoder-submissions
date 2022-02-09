#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, m; cin >> n >> m;
  vector<pair<int, int>> ab(n);
  for (int i = 0; i < n; i++) {
    int a, b; cin >> a >> b;
    ab[i] = make_pair(a, b);
  }
  sort(ab.begin(), ab.end());
  long long tot = 0;
  long long res = 0;
  for (auto &s: ab) {
    long long a = s.first, b = s.second;
    if (m <= tot + b) {
      res += a * (m - tot);
      break;
    } else {
      res += a * b;
      tot += b;
    }
  }
  cout << res << '\n';
  return 0;

}
