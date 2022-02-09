#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  map<string, int> cnt;
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    cnt[s]++;
  }
  int m;
  cin >> m;
  for (int i = 0; i < m; i++) {
    string t;
    cin >> t;
    cnt[t]--;
  }
  int res = 0;
  for (auto &sc : cnt) {
    res = max(res, sc.second);
  }
  cout << res << '\n';
  return 0;

}
