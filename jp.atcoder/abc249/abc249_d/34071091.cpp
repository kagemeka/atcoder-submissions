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
    for(int j = i; j < k; j += i) { res += (long)cnt[i] * cnt[j] * cnt[j / i]; }
  }
  cout << res << endl;
}
