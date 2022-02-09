#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  string s; cin >> s;
  vector<int> cnt(2);
  for (auto &c : s) cnt[c-'0']++;
  cout << min(cnt[0], cnt[1]) * 2<< '\n';
  return 0;
}
