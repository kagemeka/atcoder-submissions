#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b;
  cin >> a >> b;
  if(a > b) swap(a, b);
  int d = b - a;
  cout << min(d, 10 - d) << endl;
}
