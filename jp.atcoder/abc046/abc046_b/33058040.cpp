#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  int p = k;
  for(int i = 0; i < n - 1; i++) p *= (k - 1);
  cout << p << endl;
}
