#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  long k;
  cin >> n >> k;
  vector<long> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  map<long, int> cnt;
  cnt[0]++;
  for(int i = 0; i < n - 1; i++) a[i + 1] += a[i];
  long tot = 0;
  for(int i = 0; i < n; i++) {
    tot += cnt[a[i] - k];
    cnt[a[i]]++;
  }
  cout << tot << endl;
}
