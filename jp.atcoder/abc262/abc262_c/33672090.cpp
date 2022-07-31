#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  long s = 0;
  long c = 0;
  for(int i = 0; i < n; i++) { c += a[i] == i + 1; }
  s += c * (c - 1) >> 1;
  for(int i = 0; i < n; i++) {
    int j = a[i] - 1;
    if(j <= i) continue;
    s += a[j] == i + 1;
  }
  cout << s << endl;
}
