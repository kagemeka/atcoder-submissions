#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  // s[j] - s[j] = j - i (mod k)
  int n, k;
  cin >> n >> k;
  vector<int> s(n + 1);
  for(int i = 0; i < n; i++) cin >> s[i + 1];
  for(int i = 0; i < n; i++) {
    s[i + 1] += s[i];
    s[i + 1] %= k;
  }
  for(int i = 0; i < n + 1; i++) s[i] = ((s[i] - i) % k + k) % k;
  map<int, int> cnt;
  long tot = 0;
  for(int i = 0, j = 0; i < n + 1; i++) {
    for(; j <= i - k; j++) cnt[s[j]]--;
    tot += cnt[s[i]];
    cnt[s[i]]++;
  }
  cout << tot << endl;
}
