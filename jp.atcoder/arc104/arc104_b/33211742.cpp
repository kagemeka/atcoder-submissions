#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  // a = t, c = t (count)
  // a := a - t, b := c - t;
  int n;
  string s;
  cin >> n >> s;
  vector<int> a(n + 1), b(n + 1);
  for(int i = 0; i < n; i++) {
    if(s[i] == 'A') a[i + 1] += 1;
    if(s[i] == 'T') a[i + 1] -= 1;
    if(s[i] == 'C') b[i + 1] += 1;
    if(s[i] == 'G') b[i + 1]--;
  }
  for(int i = 0; i < n; i++) a[i + 1] += a[i];
  for(int i = 0; i < n; i++) b[i + 1] += b[i];
  int cnt = 0;
  for(int i = 0; i < n + 1; i++) {
    for(int j = 0; j < i; j++) { cnt += a[i] == a[j] && b[i] == b[j]; }
  }
  cout << cnt << endl;
}
