#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b;
  cin >> a >> b;
  string s = "", t = "";
  for (int i = 0; i < b; i++) s += to_string(a);
  for (int i = 0; i < a; i++) t += to_string(b);
  string ans = min(s, t);
  cout << ans << '\n';
  return 0;
}
