#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c, d;
  cin >> a >> b >> c >> d;

  cout << max(0, min(b, d) - max(a, c)) << '\n';
  return 0;

}
