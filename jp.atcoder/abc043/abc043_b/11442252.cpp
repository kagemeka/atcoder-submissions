#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;

  string res = "";
  for (char &c : s) {
    if (c != 'B') {
      res += c;
      continue;
    }
    if (res.empty()) continue;
    res.pop_back();
  }
  cout << res << '\n';
  return 0;
}