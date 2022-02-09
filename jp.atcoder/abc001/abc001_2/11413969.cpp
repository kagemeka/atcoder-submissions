#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  double m;
  cin >> m;
  m *= 0.001;

  string ans;
  if (m < 0.1) {
    ans = "00";
  } else if (m <= 5) {
    m *= 10;
    ans = (m < 10) ? to_string(m) : "0" + to_string(m);
  } else if (m <= 30) {
    ans = to_string(m + 50);
  } else if (m <= 70) {
    m = (m - 30) / 5 + 80;
    ans = to_string(m);
  } else {
    ans = "89";
  }
  cout << ans.substr(0, 2) << endl;
  return 0;
}
