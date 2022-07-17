#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int a, b;
  cin >> a >> b;
  int cnt = a;
  cnt -= b < a;
  cout << cnt << endl;
}
