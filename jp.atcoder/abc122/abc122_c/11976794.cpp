#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n, q;
  string s;
  cin >> n >> q >> s;
  vector<int> res(n);
  for (int i = 0; i < n - 1; i++) {
    res[i+1] = s.substr(i, 2) == "AC";
  }
  for (int i = 0; i < n - 1; i++) {
    res[i+1] += res[i];
  }
  for (int i = 0; i < q; i++) {
    int l, r; cin >> l >> r;
    cout << res[r-1] - res[l-1] << '\n';
  }
  return 0;
}
