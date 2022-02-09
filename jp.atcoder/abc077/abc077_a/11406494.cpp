#include <bits/stdc++.h>
using namespace std;

int main() {
  string s, t;
  cin >> s >> t;
  reverse(t.begin(), t.end());
  string ans = (s == t) ? "YES" : "NO";
  cout << ans << endl;
  return 0;
}
