#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;
  vector<long long> a(n + 1);
  for (int i = 1; i < n + 1; i++) cin >> a[i];
  for (int i = 0; i < n; i++) a[i+1] += a[i];
  for (int i = 0; i < n; i++) a[i+1] += a[i];
  cout << a[n] - a[n-(n-k+1)] - a[n-k] << '\n';
  return 0;
}
