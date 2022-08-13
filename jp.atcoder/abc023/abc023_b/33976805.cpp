#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  string s;
  cin >> n >> s;
  if(~n & 1) {
    cout << -1 << endl;
    return 0;
  }
  string t = "bac";
  int m = (n - 1) >> 1;
  int i = m % 3;
  for(int j = 0; j < n; j++, i = ((i - 1) % 3 + 3) % 3) {
    if(s[j] != t[i]) {
      cout << -1 << endl;
      return 0;
    }
  }
  cout << m << endl;
}
