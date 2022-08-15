#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 1 << 18;
  vector<int> cnt(k);
  for(auto& x: a) cnt[x]++;
  long res = 0;
  for(int i = 1; i < k; i++) {
    vector<int> divs;
    for(int j = 1; j * j <= i; j++) {
      if(i % j) continue;
      divs.push_back(j);
      if(j * j != i) divs.push_back(i / j);
    }
    for(auto& d: divs) { res += (long)cnt[d] * cnt[i / d] * cnt[i]; }
  }
  cout << res << endl;
}
