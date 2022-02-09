#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  int ans = n;
  int y;
  for (int x = 1; x < floor(sqrt(n)) + 1; x++) {
    y = n / x;
    ans = min(ans, y - x + n - y*x);
  }
  cout << ans << '\n';
  return 0;
}
