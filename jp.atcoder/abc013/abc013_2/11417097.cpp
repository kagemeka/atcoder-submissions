#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b;
  cin >> a >> b;
  int d;
  if (a == b) d = 0;
  else if (a > b) d = min(b + 10 - a, a - b);
  else d = min(b - a, a - (b - 10));
  cout << d << '\n';
  return 0;
}
