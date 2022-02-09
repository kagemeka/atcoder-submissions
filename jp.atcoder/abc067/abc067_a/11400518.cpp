#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  string ans = (a % 3 && b % 3 && (a + b) % 3) ? "Impossible" : "Possible";
  cout << ans << endl;
  return 0;
}
