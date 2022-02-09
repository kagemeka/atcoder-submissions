#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int k, n; cin >> k >> n;
  vector<int> a(n + 1);
  for (int i = 0; i < n; i++) cin >> a[i];
  a[n] = a[0] + k;
  vector<int> d(n);
  for (int i = 0; i < n; i++) d[i] = a[i+1] - a[i];
  cout << k - *max_element(d.begin(), d.end()) << '\n';
  return 0;
}
