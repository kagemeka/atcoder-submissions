#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  int m = n * 2;
  cout << m << endl;
  string x;
  while(n >= 4) {
    x += '4';
    n -= 4;
  }
  if(n) { x += to_string(n); }
  reverse(x.begin(), x.end());
  cout << x << endl;
}
