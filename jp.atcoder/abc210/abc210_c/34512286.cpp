#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  map<int, int> cnt;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  for(int i = 0; i < k; i++) cnt[a[i]]++;
  int mx = cnt.size();
  for(int i = k; i < n; i++) {
    if(--cnt[a[i - k]] == 0) { cnt.erase(a[i - k]); }
    cnt[a[i]]++;
    mx = max(mx, (int)cnt.size());
  }
  cout << mx << endl;
}
