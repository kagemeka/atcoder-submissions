
#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  using p = pair<int, string>;
  vector<p> ts(n);
  for(int i = 0; i < n; i++) {
    string s;
    int t;
    cin >> s >> t;
    ts[i] = {t, s};
  }
  sort(ts.begin(), ts.end());
  cout << ts[n - 2].second << endl;
}
