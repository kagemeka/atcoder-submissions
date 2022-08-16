#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long a, b, k;
  cin >> a >> b >> k;
  int cnt = 0;
  while(a < b) {
    cnt++;
    a *= k;
  }
  cout << cnt << endl;
}
