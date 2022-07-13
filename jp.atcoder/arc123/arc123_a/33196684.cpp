#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  long a, b, c;
  cin >> a >> b >> c;
  long cnt = 0;
  a += c;
  if(a & 1) {
    a++;
    cnt++;
  }
  cnt += abs(b - a / 2) * (1 + (a < 2 * b));
  cout << cnt << endl;
}
