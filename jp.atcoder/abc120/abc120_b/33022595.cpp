#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int a, b, k;
  cin >> a >> b >> k;

  int x = 200;
  while(true) {
    if(a % x == 0 && b % x == 0) {
      k--;
      if(k == 0) {
        cout << x << endl;
        return 0;
      }
    }
    x--;
  }
}