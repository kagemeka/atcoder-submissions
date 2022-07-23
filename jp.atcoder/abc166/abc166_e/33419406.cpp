#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  int n;
  cin >> n;
  vector<int> a(n);
  for(int i = 0; i < n; i++) { cin >> a[i]; }
  map<int, int> cnt;
  long tot = 0;
  for(int i = 0; i < n; i++) {
    tot += cnt[i - a[i]];
    cnt[i + a[i]]++;
  }
  cout << tot << endl;
}
