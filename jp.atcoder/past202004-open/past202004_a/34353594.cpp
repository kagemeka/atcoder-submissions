#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  string s, t;
  cin >> s >> t;
  auto f = [&](string s) -> int {
    if(s[0] == 'B') return -(s[1] - '0');
    return s[0] - '0' - 1;
  };
  int a = f(s);
  int b = f(t);
  cout << abs(a - b) << endl;
}
