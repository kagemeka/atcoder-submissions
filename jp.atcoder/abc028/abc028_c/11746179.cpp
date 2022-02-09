#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c, d, e;
  cin >> a >> b >> c >> d >> e;
  cout << max(a + d + e, b + c + e) << '\n';
  return 0;
}
