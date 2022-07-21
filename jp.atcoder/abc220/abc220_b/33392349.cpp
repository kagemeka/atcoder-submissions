#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int k;
  cin >> k;
  string a, b;
  cin >> a >> b;
  auto convert = [&](string s) -> int {
    int p = 1;
    int n = 0;
    reverse(s.begin(), s.end());
    for(auto& c: s) {
      int d = c - '0';
      n += d * p;
      p *= k;
    }
    return n;
  };
  cout << (long)convert(a) * convert(b) << endl;
}
