#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];
  sort(a.begin(), a.end());
  int m = n / 2;
  for (int i = 0; i < m; i++) cout << a[m] << '\n';
  for (int i = 0; i < m; i++) cout << a[m-1] << '\n';
}
