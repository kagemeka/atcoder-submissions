#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  long res = 0;
  long r, g, b;
  r = count(s.begin(), s.end(), 'R');
  g = count(s.begin(), s.end(), 'G');
  b = count(s.begin(), s.end(), 'B');
  res = r * g * b;
  for(int i = 0; i < n; i++) {
    for(int d = 1; i + 2 * d < n; d++) {
      int j = i + d;
      int k = j + d;
      res -= s[i] != s[j] && s[j] != s[k] && s[k] != s[i];
    }
  }
  cout << res << endl;
}
