#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  int n = s.size();
  long tot = (long)(n - 1) * n;
  for(int i = 0; i < n; i++) { tot += (s[i] == 'U') ? i : (n - 1 - i); }
  cout << tot << endl;
}
