#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  string s;
  int k;
  cin >> s >> k;
  int n = s.size();
  vector<int> a(n + 1);
  for(int i = 0; i < n; i++) a[i + 1] = s[i] == '.';
  for(int i = 0; i < n; i++) a[i + 1] += a[i];
  int mx = 0;
  for(int l = 0, r = 0, c = -1; l <= n; l++) {
    while(r <= n && a[r] <= a[l] + k) {
      c++;
      r++;
    }
    mx = max(mx, c);
    c--;
  }
  cout << mx << endl;
}
