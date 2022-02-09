#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c, d, e, f;
  cin >> a >> b >> c >> d;
  e = a + b;
  f = c + d;
  string ans;
  if (e > f) {
    ans = "Left";
  } else if (e < f) {
    ans = "Right";
  } else {
    ans = "Balanced";
  }
  cout << ans << endl;
  return 0;
}
