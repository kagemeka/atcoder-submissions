#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  long x = n / k;
  if(k & 1) {
    cout << x * x * x << endl;
  } else {
    long y = n / (k >> 1);
    y -= x;
    cout << x * x * x + y * y * y << endl;
  }
}
