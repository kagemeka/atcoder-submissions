#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  string s;
  cin >> s;
  cout << (s[0] == 'A' && s[n - 1] == 'B' ? "No" : "Yes") << endl;
}
