#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, k, q; cin >> n >> k >> q;
  vector<int> res(n, k - q);
  for (int i = 0; i < q; i++) {
    int a; cin >> a; a--;
    res[a]++;
  }
  for (int i = 0; i < n; i++) {
    string ans = (res[i] > 0) ? "Yes" : "No";
    cout << ans << '\n';
  }
  return 0;
}
