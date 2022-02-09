#include <bits/stdc++.h>
using namespace std;

int main() {
  double a, b, c, d;
  cin >> a >> b >> c >> d;
  double e, f;
  e = b / a; f = d / c;
  string ans;
  if (e > f) {
    ans = "TAKAHASHI";
  } else if (e == f) {
    ans = "DRAW";
  } else {
    ans = "AOKI";
  }
  cout << ans << endl;
  return 0;
}
