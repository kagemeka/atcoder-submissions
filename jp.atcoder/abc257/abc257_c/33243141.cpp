#include <bits/stdc++.h>
using namespace std;
auto main() -> int {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int n;
  string s;
  cin >> n >> s;
  vector<int> a(n);
  for(int i = 0; i < n; i++) cin >> a[i];
  vector<int> idx(n);
  iota(idx.begin(), idx.end(), 0);
  sort(idx.begin(), idx.end(), [&](int i, int j) {
    return a[i] != a[j] ? a[i] < a[j] : s[i] != s[j] ? s[i] > s[j] : i < j;
  });
  vector<int> b(n);
  for(int i = 0; i < n; i++) { b[i] = (s[idx[i]] - '0') * (-2) + 1; }
  int mx = count(b.begin(), b.end(), -1);
  for(int i = 0; i < n - 1; i++) b[i + 1] += b[i];
  cout << mx + max(*max_element(b.begin(), b.end()), 0) << endl;
}
