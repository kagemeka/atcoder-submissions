#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string s, t;
  cin >> n >> s >> t;
  string res = "";
  for (int i = 0; i < n; i++) {
    res += s[i];
    res += t[i];
  }
  cout << res << '\n';
  return 0;
}
