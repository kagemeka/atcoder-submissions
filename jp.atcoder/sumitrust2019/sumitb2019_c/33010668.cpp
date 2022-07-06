#include <bits/stdc++.h>
using namespace std;

auto main() -> int {
  int x;
  cin >> x;

  cout << (x % 100 <= x / 100 * 5) << endl;
}