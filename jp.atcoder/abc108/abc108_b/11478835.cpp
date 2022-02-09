#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int a, b, c, d, e, f, g, h;
  cin >> a >> b >> c >> d;
  e = c - (d - b);
  f = d + (c - a);
  g = e - (f - d);
  h = f + (e - c);
  cout << e << ' ';
  cout << f << ' ';
  cout << g << ' ';
  cout << h << '\n';
  return 0;
}
