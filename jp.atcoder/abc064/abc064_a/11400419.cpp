#include <bits/stdc++.h>
using namespace std;

int main() {
  int r, g, b;
  cin >> r >> g >> b;
  int a = 10 * g + b;
  string ans = (a % 4) ? "NO" : "YES";
  cout << ans << endl;
  return 0;

}
