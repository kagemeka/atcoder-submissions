#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> p(n);
  for(int i = 0; i < n; i++) cin >> p[i];
  vector<int> cnt(n);
  for(int i = 0; i < n; i++) cnt[(i - p[i] + n) % n]++;
  int mx = 0;
  for(int i = 0; i < n; i++) {
    mx = max(mx, cnt[i] + cnt[(i + 1) % n] + cnt[(i + 2) % n]);
  }
  cout << mx << endl;
}
