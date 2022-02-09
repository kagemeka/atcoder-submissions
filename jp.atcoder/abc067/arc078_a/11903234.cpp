#include <bits/stdc++.h>
using namespace std;
long long INF = numeric_limits<long long>::max();

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<long long> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  for (int i = 0; i < n - 1; i++) a[i+1] += a[i];
  long long res = INF;
  for (int i = 0; i < n - 1; i++) {
    res = min(res, abs(a[n-1] - a[i] * 2));
  }
  cout << res << '\n';
  return 0;
}
