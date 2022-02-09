#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;
  int n = s.size();
  string res = s[0] + to_string(n-2) + s[n-1];
  cout << res << '\n';
  return 0;
}
