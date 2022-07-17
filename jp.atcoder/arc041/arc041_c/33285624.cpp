#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, l;
  cin >> n >> l;
  using p = pair<int, char>;
  vector<p> a(n + 4);
  a[0] = {-1, 'R'};
  a[1] = {0, 'L'};
  for(int i = 0; i < n; i++) { cin >> a[i + 2].first >> a[i + 2].second; }
  a[n + 2] = {l + 1, 'R'};
  a[n + 3] = {l + 2, 'L'};
  n += 4;
  long tot = 0;
  int i = 0;
  while(i < n) {
    int cl = 0, cr = 0;
    int prev = -2;
    long sl = 0, sr = 0;
    while(a[i].second == 'R') {
      int x = a[i].first;
      sr += (long)(x - prev - 1) * cr;
      prev = x;
      cr++;
      i++;
    }
    int r = prev;
    int l = a[i].first;
    while(i < n && a[i].second == 'L') { i++; }
    int i0 = i;
    i--;
    while(a[i].second == 'L') {
      int x = a[i].first;
      sl += (long)(prev - x - 1) * cl;
      prev = x;
      cl++;
      i--;
    }
    long d = l - r - 1;
    sr += d * cr;
    sl += d * cl;
    tot += max(sl, sr);
    i = i0;
  }
  cout << tot << endl;
}
