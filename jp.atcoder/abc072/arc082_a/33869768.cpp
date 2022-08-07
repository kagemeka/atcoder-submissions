#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  int const k = 1 << 17;
  vector<int> cnt(k);
  while(n--) {
    int x;
    cin >> x;
    cnt[x]++;
  }
  int mx = 0;
  for(int i = 1; i < k - 1; i++) {
    mx = max(mx, cnt[i - 1] + cnt[i] + cnt[i + 1]);
  }
  cout << mx << endl;
}
