#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string s;
  cin >> n >> s;
  vector<int> cnt(3);
  for (int i = 0; i < n; i++) {
    if (s[i] == 'R') cnt[0]++;
    else if (s[i] == 'G') cnt[1]++;
    else if (s[i] == 'B') cnt[2]++;
  }
  int res = 0;
  res += cnt[0] * cnt[1] * cnt[2];
  for (int i = 0; i < n - 2; i ++) {
    for (int j = i + 1; 2 * j - i < n; j++) {
      int k = 2 * j - i;
      res -= s[i] != s[j] && s[j] != s[k] && s[k] != s[i];
    }
  }
  cout << res << '\n';
  return 0;
}
