#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  cout << (1 + n) * n / 2 * k * 100 + (1 + k) * k / 2 * n << endl;
}
