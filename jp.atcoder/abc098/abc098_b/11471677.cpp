#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string s;
  cin >> n >> s;
  vector<int> l(n);
  l[0] = 1 << (s[0] - 'a');
  vector<int> r(n);
  r[n-1] = 1 << (s[n-1] - 'a');
  for (int i = 1; i < n; i++) {
    l[i] = l[i-1] | (1 << (s[i] - 'a'));
    r[n-1-i] = r[n-i] | (1 << s[n-1-i] - 'a');
  }
  int res = 0;
  for (int i = 0; i < n - 1; i++) {
    int co = l[i] & r[i+1];
    int cnt = 0;
    for (int j = 0; j < 26; j++) {
      cnt += co >> j & 1;
    }
    res = max(res, cnt);
  }
  cout << res << '\n';
  return 0;
}
