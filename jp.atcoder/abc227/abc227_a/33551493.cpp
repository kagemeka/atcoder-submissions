#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k, a;
  cin >> n >> k >> a;
  cout << ((a - 1 + k - 1) % n + n) % n + 1 << endl;
}
