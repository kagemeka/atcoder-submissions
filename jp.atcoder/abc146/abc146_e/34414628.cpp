#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n, k;
  cin >> n >> k;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<long> s(n + 1);
  for(int i = 0; i < n; i++) s[i + 1] = s[i] + a[i];
  for(int i = 0; i < n + 1; i++) s[i] = ((s[i] - i) % k + k) % k;
  map<long, int> cnt;
  long tot = 0;
  for(int l = 0, i = 0; i < n + 1; i++) {
    if(l <= i - k) {
      cnt[s[l]]--;
      l++;
    }
    tot += cnt[s[i]]++;
  }
  cout << tot << endl;
}
