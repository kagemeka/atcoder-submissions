#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  long k;
  cin >> n >> k;
  int const m = 1 << 17;
  vector<int> cnt(m);
  for(int i = 0; i < n; i++) {
    int a, b;
    cin >> a >> b;
    cnt[a] += b;
  }
  for(int i = 0; i < m; i++) {
    k -= cnt[i];
    if(k <= 0) {
      cout << i << endl;
      return 0;
    }
  }
}
