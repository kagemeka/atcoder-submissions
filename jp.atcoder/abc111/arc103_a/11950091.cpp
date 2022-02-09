#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int U = 1e5;
  int n; cin >> n;
  vector<int> v(n);
  for (int i = 0; i < n; i++) cin >> v[i];
  vector<int> a(U + 1);
  vector<int> b(U + 1);
  for (int i = 0; i < n; i += 2) a[v[i]]++;
  for (int i = 1; i < n; i += 2) b[v[i]]++;
  vector<vector<int>> c1;
  vector<vector<int>> c2;
  for (int i = 0; i < U + 1; i++) {
    if (a[i]) c1.push_back({a[i], i});
    if (b[i]) c2.push_back({b[i], i});
  }
  sort(c1.begin(), c1.end(), greater<vector<int>>());
  sort(c2.begin(), c2.end(), greater<vector<int>>());
  if (c1.size() > c2.size()) swap(c1, c2);
  int res;
  if (c1[0][1] != c2[0][1]) res = n - c1[0][0] - c2[0][0];
  else {
    if (c2.size() == 1) res = n / 2;
    else {
      if (c1.size() == 1) res = n - c1[0][0] - c2[1][0];
      else {
        res = n - max(c1[0][0] + c2[1][0], c1[1][0] + c2[0][0]);
      }
    }
  }
  cout << res << '\n';
  return 0;
}
