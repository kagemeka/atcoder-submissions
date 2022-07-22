#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, mx, mn;
  cin >> n >> mx >> mn;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  queue<int> max_idx, min_idx;
  long cnt = 0;
  for(int l = 0, r = 0; l < n; l++) {
    if(a[l] < mn || a[l] > mx) continue;
    r = max(r, l);
    while(r < n && mn <= a[r] && a[r] <= mx) {
      if(a[r] == mn) min_idx.push(r);
      if(a[r] == mx) max_idx.push(r);
      r++;
    }
    if(min_idx.size() && max_idx.size()) {
      int i = max(min_idx.front(), max_idx.front());
      cnt += r - i;
    }
    if(min_idx.size() && min_idx.front() == l) { min_idx.pop(); }
    if(max_idx.size() && max_idx.front() == l) { max_idx.pop(); }
  }
  cout << cnt << endl;
}
