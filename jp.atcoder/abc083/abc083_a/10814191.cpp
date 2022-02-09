#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c, d;
  cin >> a >> b >> c >> d;
  int l, r;
  l = a + b;
  r = c + d;
  string ans;
  if (l > r) {
    ans = "Left";

  } else if (l < r) {
    ans = "Right";
  } else {
    ans = "Balanced";
  }
  cout << ans << endl;
}
