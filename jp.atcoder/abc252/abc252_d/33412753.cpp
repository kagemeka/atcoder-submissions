#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  int const k = 1 << 18;
  vector<long> cnt(k);
  for(auto& x: a) cnt[x]++;
  for(int i = 0; i < k - 1; i++) cnt[i + 1] += cnt[i];
  long s = 0;
  for(auto& x: a) { s += cnt[x - 1] * (n - cnt[x]); }
  cout << s << endl;
}
