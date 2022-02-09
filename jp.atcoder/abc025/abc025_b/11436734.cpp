#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, a, b;
  cin >> n >> a >> b;
  int x = 0;
  string s;
  int d;
  for (int i = 0; i < n; i++) {
    cin >> s >> d;
    if (s == "East") x += max(a, min(d, b));
    else x -= max(a, min(d, b));
  }
  if (x == 0) cout << 0 << '\n';
  else {
    if (x > 0) s = "East";
    else {
      s = "West";
      x = -x;
    }
    cout << s << " " << x << '\n';
  }
  return 0;
}
