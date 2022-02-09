#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> x(n);
  for (int i = 0; i < n; i++) cin >> x[i];
  auto a = x;
  sort(a.begin(), a.end());
  int m = n / 2;
  int l = a[m-1], r = a[m];
  for (int i = 0; i < n; i++) {
    int res = (x[i] >= r) ? l : r;
    cout << res << '\n';
  }
  return 0;
}
