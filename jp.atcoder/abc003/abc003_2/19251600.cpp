#include <bits/stdc++.h>
using namespace std;


void solve() {
  string s, t;
  cin >> s >> t;
  set<char> atcoder;
  for (
    const char& c: "atcoder"s
  ) {
    atcoder.insert(c);
  }
  for (
    int i = 0;
    i < (int)s.size();
    i++
  ) {
    if (s[i] == t[i]) continue;
    if (
      s[i] == '@' &&
      atcoder.count(t[i])
    ) continue;
    if (
      t[i] == '@' &&
      atcoder.count(s[i])
    ) continue;
    cout << "You will lose"
      << '\n';
    return;
  }
  cout << "You can win" << '\n';
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t = 1;
  while (t--) {
    solve();
  }

  return 0;
}
