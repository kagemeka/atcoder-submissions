#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int n = s.size();
  int res = 0;
  for (int i = 1; i <= (n - 1) / 2; i++) {
    if (s.substr(0, i) == s.substr(i, i)) res = i * 2;
  }
  cout << res << '\n';
  return 0;
}
