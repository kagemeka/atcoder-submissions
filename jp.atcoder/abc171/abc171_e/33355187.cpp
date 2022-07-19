#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int s = 0;
  for(auto& x: a) s ^= x;
  for(int i = 0; i < n; i++) cout << (s ^ a[i]) << " \n"[i == n - 1];
}
