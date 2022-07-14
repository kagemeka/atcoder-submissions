#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  int n = s.size();
  int k = n >> 1;
  int k0 = k;
  for(; k < n && s[k] == s[k0] && s[k] == s[n - 1 - k]; k++)
    ;
  cout << k << endl;
}
