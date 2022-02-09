#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;
  vector<int> a(n+1);
  for (int i = 0; i < n; i++) {cin >> a[i+1]; a[i+1] += a[i];}
  if (a[n] % n) {cout << -1 << '\n'; return 0;}

  int tot = 0;
  int q = a[n] / n;
  int l = 1;
  for (int r = 1; r < n + 1; r++) {
    if ((a[r] - a[l-1]) == q * (r - l + 1)) {
      tot += r - l;
      l = r + 1;
    }
  }
  cout << tot << '\n';
  return 0;
}
