#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, m;
  cin >> n >> m;
  map<int, int> cnt;
  for(int i = 0; i < n; i++) {
    int x;
    cin >> x;
    cnt[x]++;
  }
  vector<int> b(m);
  for(int i = 0; i < m; i++) cin >> b[i];
  for(auto& x: b) {
    if(cnt[x] > 0) {
      cnt[x]--;
      continue;
    }
    cout << "No" << endl;
    return 0;
  }
  cout << "Yes" << endl;
}
