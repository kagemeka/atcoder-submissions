#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  auto b = a;
  sort(b.begin(), b.end(), greater<int>());
  for (auto &x : a) {
    int ans = (x == b[0]) ? b[1] : b[0];
    cout << ans << '\n';
  }
  return 0;


}
