#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int n; cin >> n;
  vector<int> b(n + 1); b[0] = b[n] = 1001001001;
  for (int i = 1; i < n; i++) cin >> b[i];
  vector<int> a(n);
  for (int i = 0; i < n; i++) a[i] = min(b[i], b[i+1]);
  int s = 0;
  for (auto &x : a) s += x;
  cout << s << '\n';
  return 0;
}
