#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> k(n - 1);
  for(int i = 0; i < n - 1; i++) cin >> k[i];
  vector<int> a(n);
  a[0] = k[0];
  a[n - 1] = k[n - 2];
  for(int i = 0; i < n - 2; i++) { a[i + 1] = min(k[i], k[i + 1]); }
  for(int i = 0; i < n; i++) { cout << a[i] << " \n"[i == n - 1]; }
}
