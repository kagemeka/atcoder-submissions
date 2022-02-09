#include <bits/stdc++.h>
using namespace std;

int main() {
  int x, a, b;
  cin >> x >> a >> b;
  string ans = (abs(a - x) > abs(b - x)) ? "B" : "A";
  cout << ans << endl;
  return 0;
}
