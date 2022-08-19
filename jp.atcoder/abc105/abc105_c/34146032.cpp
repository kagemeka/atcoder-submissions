#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  if(n == 0) {
    cout << 0 << endl;
    return 0;
  }
  vector<int> res;
  int b = -2;
  while(n) {
    int q = n / b;
    int r = n % b;
    if(r < 0) {
      r -= b;
      q++;
    }
    res.push_back(r);
    n = q;
  }
  reverse(res.begin(), res.end());
  for(auto& x: res) { cout << x; }
  cout << endl;
}
