#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s;
  cin >> s;
  vector<int> c(26);
  for(auto& x: s) c[x - 'a'] ^= 1;
  cout << (accumulate(c.begin(), c.end(), 0) == 0 ? "Yes" : "No") << endl;
}
