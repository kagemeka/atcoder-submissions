#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n, m;
  cin >> n >> m;
  vector<int> a(n), b(n);
  for(int i = 0; i < n; i++) cin >> a[i] >> b[i];
  vector<int> cnt(n);
  vector<vector<int>> que(m);
  for(int i = 0; i < n; i++) {
    a[i]--;
    b[i]--;
    que[a[i]].push_back(i);
    que[b[i]].push_back(i);
  }
  vector<int> res(m + 2);
  for(int l = 0, r = 0, now = 0; l < m; l++) {
    while(r < m && now < n) {
      for(int& i: que[r]) {
        cnt[i]++;
        if(cnt[i] == 1) now++;
      }
      r++;
    }
    if(r == m && now < n) break;
    res[r - l]++;
    res[m - l + 1]--;
    for(int& i: que[l]) {
      cnt[i]--;
      if(cnt[i] == 0) now--;
    }
  }
  for (int i = 0; i < m + 1; i++) {
    res[i + 1] += res[i];
  }
  for (int i = 0; i < m; i++) {
    cout << res[i + 1] <<" \n"[i == m - 1];
  }
}
