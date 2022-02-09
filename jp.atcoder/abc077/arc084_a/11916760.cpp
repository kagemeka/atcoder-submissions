#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  vector<int> b(n);
  for (int i = 0; i < n; i++) cin >> b[i];
  vector<int> c(n);
  for (int i = 0; i < n; i++) cin >> c[i];
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  sort(c.begin(), c.end());
  long long combs = 0;
  for (auto x : b) {
    int i, j;
    i = lower_bound(a.begin(), a.end(), x) - a.begin();
    j = upper_bound(c.begin(), c.end(), x) - c.begin();
    combs += (long long)i * (n - j);
  }
  cout << combs << '\n';
  return 0;
}
