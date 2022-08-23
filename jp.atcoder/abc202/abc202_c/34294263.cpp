#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n), b(n), c(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < n; i++) cin >> b[i];
  for(int i = 0; i < n; i++) cin >> c[i];
  for(int i = 0; i < n; i++) {
    a[i]--;
    b[i]--;
    c[i]--;
  }
  int const k = 1 << 17;
  vector<int> ca(k), cb(k);
  for(int i = 0; i < n; i++) ca[a[i]]++;
  for(int i = 0; i < n; i++) cb[b[c[i]]]++;
  long s = 0;
  for(int i = 0; i < k; i++) { s += (long)ca[i] * cb[i]; }
  cout << s << endl;
}
