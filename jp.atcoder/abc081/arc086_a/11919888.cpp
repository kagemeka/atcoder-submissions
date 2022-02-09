#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k; cin >> n >> k;
  vector<int> cnt(n);
  for (int i = 0; i < n; i++) {
    int a; cin >> a; a--;
    cnt[a]++;
  }
  vector<int> res;
  for (int i = 0; i < n; i++) {
    if (cnt[i]) res.push_back(cnt[i]);
  }
  sort(res.begin(), res.end(), greater<int>());
  int ans = 0;
  for (int i = k; i < res.size(); i++) {
    ans += res[i];
  }
  cout << ans << '\n';
  return 0;
}
