#include <bits/stdc++.h>
using namespace std;

int main() {
  map<string, int> cnt;

  int n;
  cin >> n;
  vector<string> s(n);
  for (int i = 0; i < n; i++) {
    cin >> s[i];
    cnt[s[i]]++;
  }
  int m;
  cin >> m;
  vector<string> t(m);
  for (int i = 0; i < m; i++) {
    cin >> t[i];
    cnt[t[i]]--;
  }

  int res = 0;
  for (auto kv:cnt) {
    int v = kv.second;
    res = max(res, v);
  }
  cout << res << endl;
  return 0;
}
