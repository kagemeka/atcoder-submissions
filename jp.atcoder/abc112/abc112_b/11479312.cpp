#include <bits/stdc++.h>
using namespace std;

const int INF = 100100;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, T;
  cin >> n >> T;
  vector<pair<int, int>> ct(n);
  for (int i = 0; i < n; i++) {
    int c, t;
    cin >> c >> t;
    ct[i] = make_pair(c, t);
  }
  int res = INF;
  for (int i = 0; i < n; i++) {
    if (ct[i].second <= T) {
      res = min(res, ct[i].first);
    }
  }
  if (res == INF) cout << "TLE";
  else cout << res;
  cout << '\n';
  return 0;
}
