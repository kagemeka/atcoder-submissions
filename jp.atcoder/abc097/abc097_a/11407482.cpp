#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c, d;
  cin >> a >> b >> c >> d;
  string ans = (abs(c-a) <= d || (abs(b-a) <= d && abs(c-b) <= d)) ? "Yes" : "No";
  cout << ans << endl;
  return 0;

}
