#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  cin >> s >> t;
  int n = s.size();
  int cnt = 0;
  for (int i = 0; i < n; i++) cnt += s[i] != t[i];
  cout << cnt << endl;
}
