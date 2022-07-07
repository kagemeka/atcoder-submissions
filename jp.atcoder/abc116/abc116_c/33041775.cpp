
#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> h(n);
  for(int i = 0; i < n; i++) cin >> h[i];
  int cnt = 0;
  for(int t = 0; t < 100; t++) {
    bool flg = false;
    for(int i = 0; i < n; i++) {
      if(h[i] == 0) {
        cnt += flg;
        flg = false;
      } else {
        h[i]--;
        flg = true;
      }
    }
    cnt += flg;
  }
  cout << cnt << endl;
}
