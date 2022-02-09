#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b, x;
  cin >> a >> b >> x;
  string ans = (a <= x && x <= (a + b)) ? "YES" : "NO";
  cout << ans << endl;
  return 0;
}
