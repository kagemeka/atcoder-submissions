#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<vector<int>> cnt(n, vector<int>(26));
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    for (auto &c : s) {
      cnt[i][c - 'a']++;
    }
  }
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < 26; j++) {
      cnt[i+1][j] = min(cnt[i+1][j], cnt[i][j]);
    }
  }
  string ans = "";
  for (int i = 0; i < 26; i++) {
    for (int j = 0; j < cnt[n-1][i]; j++) {
      ans += (char)('a' + i);
    }
  }
  cout << ans << '\n';
  return 0;
}
