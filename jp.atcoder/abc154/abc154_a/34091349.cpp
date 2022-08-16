#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  int a, b;
  string u;
  cin >> s >> t >> a >> b >> u;
  if(u == s) a--;
  else b--;
  cout << a << ' ' << b << endl;
}
